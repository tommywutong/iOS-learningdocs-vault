---
title: Customizing a TensorFlow operation
framework: Metal
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/customizing-a-tensorflow-operation
source_url: 'https://developer.apple.com/documentation/metal/customizing-a-tensorflow-operation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/customizing-a-tensorflow-operation.json'
content_hash: 'sha256:ed9c388b70125543'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [Metal sample code library](metal-sample-code-library.md)

# Customizing a TensorFlow operation

<sub>Sample Code</sub>

Implement a custom operation that uses Metal kernels to accelerate neural-network training performance.

## Overview

> [!note] Note
> This sample code project is associated with WWDC22 session [10063: Accelerate machine learning with Metal](https://developer.apple.com/wwdc22/10063/).

### Configure the sample code

1. Follow the instructions in [Getting started with tensorflow-metal](https://developer.apple.com/metal/tensorflow-plugin/).
2. Install ffmpeg using `brew`.

```shell
brew install ffmpeg
```

1. Install the required Python packages.

```shell
pip install -r requirements.txt
```

1. Use `make` to build the custom operation with Xcode.

```shell
cd hash_encoder
make
cd ..
```

1. Run the sample.

```shell
python tiny_nerf_hash.py
```

1. View the resutls in the `result_nerf_hash` folder.

- To compare the performance benefits provided by this sample, you can run the original NeRF sample code included with the project.  View the resutls in the `result_nerf_mlp` folder.

```shell
python tiny_nerf_mlp.py
```

> [!note] Note
> The sample uses low-resolution (100x100) images by default. You can alternatively use a high-resolution version of the data to produce a clearer rendering.

## See Also

### Compute workflows

- [Performing calculations on a GPU](performing-calculations-on-a-gpu.md) — Use Metal to find GPUs and perform calculations on them.
- [Selecting device objects for compute processing](selecting-device-objects-for-compute-processing.md) — Switch dynamically between multiple GPUs to efficiently execute a compute-intensive simulation.
- [Customizing a PyTorch operation](customizing-a-pytorch-operation.md) — Implement a custom operation in PyTorch that uses Metal kernels to improve performance.

## Download

- [CustomizingATensorFlowOperation.zip](https://docs-assets.developer.apple.com/published/da6dd297d52f/CustomizingATensorFlowOperation.zip)
