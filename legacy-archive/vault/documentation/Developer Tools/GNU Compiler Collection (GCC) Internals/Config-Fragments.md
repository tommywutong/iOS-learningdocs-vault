---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Config-Fragments.html
archived_at: '2026-07-15T07:30:59.575705Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [System Config](System-Config.md#apple-kn4xg5dfnuwug33omzuwo),
Up: [Configuration](Configuration.md#apple-inxw4ztjm52xeylunfxw4)

---

##### 6.3.2.1 Scripts Used by `configure`

`configure` uses some other scripts to help in its work:

- The standard GNU `config.sub` and `config.guess`
  files, kept in the top level directory, are used. FIXME: when is the
  `config.guess` file in the `gcc` directory (that just calls
  the top level one) used?
- The file `config.gcc` is used to handle configuration
  specific to the particular target machine. The file
  `config.build` is used to handle configuration specific to the
  particular build machine. The file `config.host` is used to handle
  configuration specific to the particular host machine. (In general,
  these should only be used for features that cannot reasonably be tested in
  Autoconf feature tests.)
  See [The `config.build`; `config.host`; and `config.gcc` Files](System-Config.md#apple-kn4xg5dfnuwug33omzuwo), for details of the contents of these files.
- Each language subdirectory has a file
  `language/config-lang.in` that is used for
  front-end-specific configuration. See [The Front End `config-lang.in` File](Front-End-Config.md#apple-izzg63tufvcw4zbninxw4ztjm4), for details of this file.
- A helper script `configure.frag` is used as part of
  creating the output of `configure`.
