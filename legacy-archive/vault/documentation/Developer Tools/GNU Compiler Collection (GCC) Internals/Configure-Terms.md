---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Configure-Terms.html
archived_at: '2026-07-15T07:30:59.594524Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Top Level](Top-Level.md#apple-krxxalkmmv3gk3a),
Up: [Source Tree](Source-Tree.md#apple-knxxk4tdmuwvi4tfmu)

---

### 6.1 Configure Terms and History

The configure and build process has a long and colorful history, and can
be confusing to anyone who doesn't know why things are the way they are.
While there are other documents which describe the configuration process
in detail, here are a few things that everyone working on GCC should
know.

There are three system names that the build knows about: the machine you
are building on (build), the machine that you are building for
(host), and the machine that GCC will produce code for
(target). When you configure GCC, you specify these with
`--build=`, `--host=`, and `--target=`.

Specifying the host without specifying the build should be avoided, as
`configure` may (and once did) assume that the host you specify
is also the build, which may not be true.

If build, host, and target are all the same, this is called a
native. If build and host are the same but target is different,
this is called a cross. If build, host, and target are all
different this is called a canadian (for obscure reasons dealing
with Canada's political party and the background of the person working
on the build at that time). If host and target are the same, but build
is different, you are using a cross-compiler to build a native for a
different system. Some people call this a host-x-host,
crossed native, or cross-built native. If build and target
are the same, but host is different, you are using a cross compiler to
build a cross compiler that produces code for the machine you're
building on. This is rare, so there is no common way of describing it.
There is a proposal to call this a crossback.

If build and host are the same, the GCC you are building will also be
used to build the target libraries (like `libstdc++`). If build and host
are different, you must have already build and installed a cross
compiler that will be used to build the target libraries (if you
configured with `--target=foo-bar`, this compiler will be called
`foo-bar-gcc`).

In the case of target libraries, the machine you're building for is the
machine you specified with `--target`. So, build is the machine
you're building on (no change there), host is the machine you're
building for (the target libraries are built for the target, so host is
the target you specified), and target doesn't apply (because you're not
building a compiler, you're building libraries). The configure/make
process will adjust these variables as needed. It also sets
`$with_cross_host` to the original `--host` value in case you
need it.

The `libiberty` support library is built up to three times: once
for the host, once for the target (even if they are the same), and once
for the build if build and host are different. This allows it to be
used by all programs which are generated in the course of the build
process.
