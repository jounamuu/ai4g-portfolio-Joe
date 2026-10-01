### 1. Cómo conseguir el archivo JSON en ComfyUI

Sí, se consigue exportándolo directamente desde la interfaz. Tienes dos formas muy sencillas:

* **Método 1 (Menú lateral de ComfyUI):**
1. En el panel flotante de controles (donde está el botón azul de *Ejecutar* / *Queue Prompt*), busca el botón **"Guardar"** o **"Save"**.
2. Al pulsarlo, el navegador descargará automáticamente un archivo llamado `workflow.json` (o te pedirá dónde guardarlo). Ese archivo es el que debes entregar.


* **Método 2 (Arrastrar la imagen generada):**
* Cada fotograma o vídeo generado por ComfyUI incrusta automáticamente el flujo en sus metadatos. Si arrastras una imagen generada al lienzo, se carga el flujo completo; aun así, para la entrega formal, el archivo `.json` del Método 1 es el estándar exigido.



---

### 2. Shot List (Official English Version for Submission)

Copia y pega este contenido en un archivo llamado `SHOTLIST.md` o inclúyelo en tu documentación de entrega:

# SDG 13: Climate Action – Short Film Shot List

* **Total Runtime:** 00:30 (6 shots × 5 seconds each)
* **Base Pipeline:** MiniMax H3 Image-to-Video Workflow (ComfyUI)
* **UNET Checkpoint:** `minimax_h3_fl2va_pruned_int8_convrot.safetensors`

* **Text Encoder (CLIP):** `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors`

* **VAE:** `minimax_h3_video_vae_int8_convrot.safetensors`

* **LoRA Model:** `minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors` (Strength: 1.0)


* **Global Turbo Settings:** `turbo_mode: true` | `turbo_steps: 8` | `aspect_ratio: 16:9`

* **Universal Negative Prompt:**
```text
moving camera, camera pan, tilt, zoom, camera shake, morphing window frame, warping architecture, cartoon, anime, 3d render, oversaturated, low quality, artifacts, blurry

```



---

### Sequence Breakdown

#### Shot 01: The Natural Origin (00:00 – 00:05)

* **Input Image:** `1.jpg` (Rustic wooden window looking at green meadow and hills)


* **Duration:** 5.0 seconds


* **Prompt:**
```text
Static camera view from inside, locked-off shot, the wooden window frame in the foreground remains completely still and motionless. Outside the window: a gentle summer breeze rustles through the vibrant green meadow grass, creating soft rippling waves. The leaves of the central tree sway naturally. High above the forested hills, fluffy white clouds drift slowly and peacefully across the sunny blue sky. Warm, pristine natural lighting, photorealistic movement.

```



#### Shot 02: Industrialization & Fossil Fuels (00:05 – 00:10)

* **Input Image:** `2.jpg` (Brick window frame looking at smoking industrial chimneys)


* **Duration:** 5.0 seconds


* **Prompt:**
```text
Static interior camera shot, the dark brick window frame and window sill remain completely frozen and solid. Outside the window: continuous, heavy grey and black industrial smoke billows vigorously from the tall factory chimneys, rising and slowly expanding into a thick, stagnant overcast sky. Subtle dark soot particles drift in the hazy air. Low-contrast diffused daylight struggling through heavy atmospheric industrial pollution.

```



#### Shot 03: The Sustainable Crossroads (00:10 – 00:15)

* **Input Image:** `4.jpg` (Modern wooden sill with potted plants, wind turbines, sunset)


* **Duration:** 5.0 seconds


* **Prompt:**
```text
Completely static indoor perspective, the clean window frame, potted plants, and wooden sill stay perfectly still. Outside across the lush green pine forest: all the white wind turbines rotate smoothly, continuously, and synchronously in the brisk wind. The tops of the pine trees sway gently. The warm golden sunset casts shifting, radiant rays of clean sunlight through the glass, soft atmospheric haze, hopeful environmental energy.

```


* *Post-production Note: Apply a 4-frame digital glitch / RGB split transition at 00:14:20 to bridge into the collapse branch.*

#### Shot 04: The Climate Tipping Point (00:15 – 00:20)

* **Input Image:** `7.jpg` (Cracked stone bunker window looking at ash eruption and crater)


* **Duration:** 5.0 seconds


* **Prompt:**
```text
Static shot from inside a damaged bunker, the rough stone window frame remains entirely motionless. Outside in the barren apocalyptic wasteland: a violent and massive eruption of dense, heavy grey ash clouds billows and surges aggressively into the atmosphere, rapidly rolling forward across the dark rocky ground. Heat haze and atmospheric turbulence distort the distant horizon. Dramatic, turbulent, heavy volcanic smoke dynamics.

```



#### Shot 05: The Scorched Earth (00:20 – 00:25)

* **Input Image:** `5.jpg` (Ruined concrete frame overlooking desert drought and dust storm)


* **Duration:** 5.0 seconds


* **Prompt:**
```text
Locked-off camera from inside the ruined room, the cracked window frame is completely still. Outside: a severe atmospheric dust storm with dense orange and reddish sand sweeps continuously across the barren, cracked earth. The dead skeletal tree branches tremble under strong desert winds. Heavy heat shimmers distort the background as thick toxic haze drifts relentlessly, blinding solar glare, total environmental devastation.

```



#### Shot 06: Extinction / Cold Void (00:25 – 00:30)

* **Input Image:** `8.jpg` (Thick orbital stone portal observing dead Earth from space)


* **Duration:** 5.0 seconds


* **Prompt:**
```text
Static perspective looking out through a thick orbital observation window, the interior stone structure is 100% frozen. Outside in the cold, silent void of deep space: the dead, barren, oceanless grey planet below rotates very slowly and subtly on its axis. Tiny, faint space dust particles drift weightlessly past the glass. Distant stars and a cold white sun cast sharp, stark contrast shadows across the cratered planetary surface. Cosmic stillness, haunting zero-gravity motion.

```