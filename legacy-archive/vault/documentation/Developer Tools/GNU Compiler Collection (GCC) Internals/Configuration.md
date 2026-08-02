---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Configuration.html
archived_at: '2026-07-15T07:30:59.588787Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Build](Build.md#apple-ij2ws3de),
Previous: [Subdirectories](Subdirectories.md#apple-kn2wezdjojswg5dpojuwk4y),
Up: [gcc Directory](gcc-Directory.md#apple-m5rwglkenfzgky3un5zhs)

---

#### 6.3.2 Configuration in the `gcc` Directory

The `gcc` directory is configured with an Autoconf-generated
script `configure`. The `configure` script is generated
from `configure.ac` and `aclocal.m4`. From the files
`configure.ac` and `acconfig.h`, Autoheader generates the
file `config.in`. The file `cstamp-h.in` is used as a
timestamp.

- [Config Fragments](Config-Fragments.md#apple-inxw4ztjm4wum4tbm5wwk3tuom): Scripts used by `configure`.
- [System Config](System-Config.md#apple-kn4xg5dfnuwug33omzuwo): The `config.build`, `config.host`, and
  `config.gcc` files.
- [Configuration Files](Configuration-Files.md#apple-inxw4ztjm52xeylunfxw4lkgnfwgk4y): Files created by running `configure`.
