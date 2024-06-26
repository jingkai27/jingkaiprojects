alert("JavaScript file loaded");
console.log("hello world");

let scene, camera, renderer, model, controls;

function init() {
    // Create scene
    scene = new THREE.Scene();

    console.log("hello world");

    // Create camera
    camera = new THREE.PerspectiveCamera(65, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.set(0, 50, -90);
    console.log("camera created")


    // Create renderer
    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('container').appendChild(renderer.domElement);
    console.log("renderer created")
    renderer.setClearColor(0xAAAAAA); // Light gray background


    const geometry = new THREE.BoxGeometry();
    const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);
    console.log("Cube added to scene");

    // Add lighting
    const ambientLight = new THREE.AmbientLight(0x404040,1.2); // Soft white light
    scene.add(ambientLight);
    console.log("AmbientLight added to scene");

    const directionalLight = new THREE.DirectionalLight(0xFEFFD2, 2); // White directional light
    directionalLight.position.set(0, 20, 12); // Position the light behind the camera to shine on the front
    directionalLight.target.position.set(0, 10, 0); // Point the light towards the center of the scene
    scene.add(directionalLight);
    scene.add(directionalLight.target);
    console.log("DirectionalLight added to scene");

    // Add orbit controls
    controls = new THREE.OrbitControls(camera, renderer.domElement);
    console.log("controls created")



    // Load model
    const loader = new THREE.GLTFLoader();
    loader.load('building.glb', (gltf) => {
        console.log("Model loaded successfully");
        model = gltf.scene;
        scene.add(model);
        animate();
    }, undefined, (error) => {
        console.error(error);
    });

    // Handle window resize
    window.addEventListener('resize', onWindowResize, false);
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

function animate() {
    requestAnimationFrame(animate);
    if (model) {
    }
    controls.update(); // Update controls
    renderer.render(scene, camera);
}

init();
