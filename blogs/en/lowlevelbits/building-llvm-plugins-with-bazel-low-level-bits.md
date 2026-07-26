---
title: Building LLVM plugins with Bazel - Low Level Bits 🇺🇦
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/building-llvm-plugins-with-bazel/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:556bed37f4f702c3'
translated: false
---

> 原文：[Building LLVM plugins with Bazel - Low Level Bits 🇺🇦](https://lowlevelbits.org/building-llvm-plugins-with-bazel/)　·　Low Level Bits (Alex Denisov)

# Building LLVM plugins with Bazel

_Published on Apr 01, 2025_

This is a mirror of the Substack article   
 [Building LLVM plugins with Bazel](https://lowlevelbits.com/p/building-llvm-plugin-with-bazel)  
 The most recent version is there.

One of the premises of [Bazel](https://bazel.build) is to provide reproducible, hermetic builds, thus you shouldn’t depend on whatever is installed on the host OS and all the dependencies typically managed by Bazel directly.

However, if you want to build plugins for LLVM (or any other project really), then you should link against the specific versions installed on the user’s system.

As I’m working on [such a plugin](https://github.com/mull-project/mull), it’s been a long “dream” of mine to migrate to Bazel for the many benefits it provides. Over time, the existing build system (CMake) has grown its capabilities and I have certain requirements for how the builds should work.Namely:

- the plugin must work on different versions of OS (Ubuntu 20.xx-24.xx, macOS)
- the plugin must support different versions of LLVM, which are different on each OS (e.g., LLVM 12 on Ubuntu 20.04, LLVM 16, 17, 18 on Ubuntu 24.04 etc)
- the plugin must be linking against the system libraries due to the ABI requirements
- the build system should support multiple versions at the same time

None of these are necessarily hard or impossible with Bazel, but the devil is always in the details.

What follows is my take on solving this problem.

Source code is available here [https://github.com/AlexDenisov/bazel-llvm-plugin](https://github.com/AlexDenisov/bazel-llvm-plugin).

> Following the [Cunningham’s Law](https://meta.wikimedia.org/wiki/Cunningham%27s_Law) I claim that there is no better way to do it.

### Detecting available LLVM versions

Third-party dependencies in Bazel are typically coming in a form of external repositories, thus all supported LLVM versions must be defined in MODULE.bazel upfront. However, what happens if the version is not supported or not installed on the host OS? In this case, these repositories must be defined dynamically.

To do so, first we need to define a custom dynamic repository which will check which versions are installed on the host OS and store this information in a global variable available for later use by different parts of the build system:

```python
# available_llvm_versions.bzl
def _is_macos(ctx):
    return ctx.os.name.find("mac") != -1

def llvm_path(ctx, version):
    if _is_macos(ctx):
        return "/opt/homebrew/opt/llvm@" + version
    return "/usr/lib/llvm-" + version

def _is_supported(repository_ctx, version):
    return repository_ctx.path(llvm_path(repository_ctx, version)).exists

def _llvm_versions_repo_impl(repository_ctx):
    available_versions = []
    for version in repository_ctx.attr.versions:
        if _is_supported(repository_ctx, version):
            available_versions.append(version)
    repository_ctx.file("llvm_versions.bzl",
        content = "AVAILABLE_LLVM_VERSIONS = " + str(available_versions),
    )
    repository_ctx.file(
        "BUILD",
        content = "",
    )

available_llvm_versions_repo = repository_rule(
    local = True,
    implementation = _llvm_versions_repo_impl,
    attrs = {
        "versions": attr.string_list(),
    },
)

def _available_llvm_versions_impl(module_ctx):
    versions = []
    for mod in module_ctx.modules:
        for data in mod.tags.detect_available:
            for version in data.versions:
                versions.append(version)
    available_llvm_versions_repo(name = "available_llvm_versions", versions = versions)

available_llvm_versions = module_extension(
    implementation = _available_llvm_versions_impl,
    tag_classes = {
        "detect_available": tag_class(attrs = {"versions": attr.string_list(allow_empty = False)}),
    },
)
```

Which must be defined in MODULE.bazel:

```python
# MODULE.bazel
SUPPORTED_LLVM_VERSIONS = ["17", "18"]

available_llvm_versions = use_extension("//:bazel/available_llvm_versions.bzl", "available_llvm_versions")
available_llvm_versions.detect_available(versions = SUPPORTED_LLVM_VERSIONS)
use_repo(available_llvm_versions, "available_llvm_versions")
```

### Defining LLVM repositories

Now, as we know which versions are available installed on the host system, we can define LLVM repositories which will expose `libLLVM.so` and all the needed headers.

This part requires a dynamic module extension which will either define a real repository, or will define a “fake” empty repo. This is needed so that all the repositories can be later defined in MODULE.bazel safely.

```python
# llvm_repos.bzl
load("@available_llvm_versions//:llvm_versions.bzl", "AVAILABLE_LLVM_VERSIONS")
load("@bazel_tools//tools/build_defs/repo:local.bzl", "new_local_repository")

def _empty_repo_impl(repository_ctx):
    repository_ctx.file(
        "BUILD",
        content = "",
    )

empty_repo = repository_rule(
    local = True,
    implementation = _empty_repo_impl,
)

def _llvm_repos_extension(module_ctx):
    """Module extension to dynamically declare local LLVM repositories."""
    for mod in module_ctx.modules:
        for data in mod.tags.configure:
            for version in data.versions:
                llvm_repo_name = "llvm_" + version
                if version not in AVAILABLE_LLVM_VERSIONS:
                    empty_repo(name = llvm_repo_name)
                    continue

                path = llvm_path(module_ctx, version)
                new_local_repository(
                    name = llvm_repo_name,
                    path = path,
                    build_file = ":third_party/LLVM/llvm.BUILD"
                )

    return modules.use_all_repos(module_ctx)

llvm_repos = module_extension(
    implementation = _llvm_repos_extension,
    tag_classes = {"configure": tag_class(attrs = {"versions": attr.string_list()})},
)
```

How we can tell Bazel that these repos are available for consumption:

```python
# MODULE.bazel
SUPPORTED_LLVM_VERSIONS = ["17", "18"]

available_llvm_versions = use_extension("//:bazel/available_llvm_versions.bzl", "available_llvm_versions")
available_llvm_versions.detect_available(versions = SUPPORTED_LLVM_VERSIONS)
use_repo(available_llvm_versions, "available_llvm_versions")

llvm_repos = use_extension(":bazel/llvm_repos.bzl", "llvm_repos")
llvm_repos.configure(versions = SUPPORTED_LLVM_VERSIONS)

[use_repo(llvm_repos, "llvm_%s" % v) for v in SUPPORTED_LLVM_VERSIONS]
```

### Defining plugin targets

Now, the rest is rather trivial. We can define all the plugin libraries depending on the LLVM versions available on the host OS:

```python
# src/BUILD
load("@available_llvm_versions//:llvm_versions.bzl", "AVAILABLE_LLVM_VERSIONS")
load("@rules_cc//cc:defs.bzl", "cc_binary")

[
    cc_binary(
        name = "llvm_plugin_%s" % llvm_version,
        srcs = [
            "plugin.cpp",
        ],
        linkshared = True,
        visibility = ["//visibility:public"],
        deps = [
            "@llvm_%s//:libllvm" % llvm_version,
        ],
    )
    for llvm_version in AVAILABLE_LLVM_VERSIONS
]
```

### Defining test targets

Obviously, we must have tests for the plugin. This is also relatively trivial, we need to define a test case for each available LLVM versions as well, thus producing NxM tests where N is the number of tests and M is the number of LLVM versions.

```python
# tests/BUILD
load("@available_llvm_versions//:llvm_versions.bzl", "AVAILABLE_LLVM_VERSIONS")
load("@bazel_itertools//lib:itertools.bzl", "itertools")
load("@pypi//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_test")

[
    py_test(
        name = "%s_%s_test" % (test, llvm_version),
        srcs = ["lit_runner.py"],
        args = [ "-v", test],
        data = [
            requirement("lit"),
            ":lit.cfg.py",
            "@llvm_%s//:clang" % llvm_version,
            "@llvm_%s//:FileCheck" % llvm_version,
            "//src:llvm_plugin_%s" % llvm_version,
            test,
        ],
        main = "lit_runner.py",
        deps = [requirement("lit"), "@rules_python//python/runfiles"],
    )
    for (test, llvm_version) in itertools.product(
        glob(["*.c"]),
        AVAILABLE_LLVM_VERSIONS,
    )
]
```

### Conclusion

With all the little pieces above, the builds are now completely transparent and smooth for the end user:

![Build & test the plugin](https://lowlevelbits.org/img/llvm-plugins-bazel/plugin-build.png)

Full working example can be found here: [https://github.com/AlexDenisov/bazel-llvm-plugin](https://github.com/AlexDenisov/bazel-llvm-plugin)
