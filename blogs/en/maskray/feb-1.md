---
title: Feb 1
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2026-02-01-lld-22-elf-changes'
original_language: en
published: 2026-02-01
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:be9aeed68158be6a'
translated: false
---

> 原文：[Feb 1](https://maskray.me/blog/2026-02-01-lld-22-elf-changes)　·　MaskRay (宋方睿)

[2026-02-01](https://maskray.me/blog/2026-02-01-lld-22-elf-changes)

# lld 22 ELF changes

For those unfamiliar, [lld](https://lld.llvm.org/) is the LLVM linker, supporting PE/COFF, ELF, Mach-O, and WebAssembly ports. These object file formats differ significantly, and each port must follow the conventions of the platform's system linker. As a result, the ports share limited code (diagnostics, memory allocation, etc) and have largely separate reviewer groups.

With LLVM 22.1 releasing soon, I've added some notes to the [https://github.com/llvm/llvm-project/blob/release/22.x/lld/docs/ReleaseNotes.rst](https://github.com/llvm/llvm-project/blob/release/22.x/lld/docs/ReleaseNotes.rst) as an lld/ELF maintainer. As usual, I've reviewed almost all the patches not authored by me.

For the first time, I used an LLM agent (Claude Code) to help look through commits (`git log release/21.x..release/22.x -- lld/ELF`) and draft the release notes. Despite my request to only read lld/ELF changes, Claude Code also crafted notes for other ports, which I retained since their release notes had been quite sparse for several releases. Changes back ported to the 21.x release are removed (`git log --oneline llvmorg-22-init..llvmorg-21.1.8 -- lld`).

I'll delve into some of the key changes.

- has been added to redirect garbage collection section listing to a file, avoiding contamination of stdout with other linker output. (

  #159706

  )
- lexer state has been added for better version script parsing. This brings the lexer behavior closer to GNU ld. (

  #174530

  )
- #168189

  )
- and

  are now recognized as RELRO sections, allowing profile-guided static data partitioning. (

  #148920

  )
- #157043

  )
- has been added to prepend an argument to the remote compiler's command line. (

  #162456

  )
- #149265

  ) (

  #151685

  )
- with synthetic sections and improved handling when patched code is far from the short jump. (

  #170495

  )
- dynamic relocation type for relocating word-sized data using the return value of a function. (

  #156564

  )
- relocation type to support deactivation symbols. (

  #133534

  )
- #147970

  )
- #165263

  )
- now synthesizes

  at input section start to preserve alignment information. (

  #153935

  )
- #172618

  ) (

  #176312

  )
- #159987

  )
- #169273

  )
- now synthesizes

  at input section start to preserve alignment information during two-stage linking. (

  #151639

  ) This is an interesting

  relocatable linking challenge

  for linker relaxation.

Besides me, Peter Smith (smithp35) and Jessica Clarke (jrtc27) have done a lot of reviews.

jrtc27 has done great work simplifying the dynamic relocation system, which is highly appreciated.

I should call out [https://github.com/llvm/llvm-project/pull/172618](https://github.com/llvm/llvm-project/pull/172618): for this relatively large addition, the author and approver are from the same company and contributing to their architecture, and neither the author nor the approver is a regular lld contributor/reviewer. The author did not request review from regular reviewers and landed the patch just 3 minutes after their colleague's approval. I left a comment asking to keep the PR open for other maintainers to review.

## Distributed ThinLTO

[Distributed ThinLTO (DTLTO)](https://llvm.org/docs/DTLTO.html) enables distributing ThinLTO backend compilations to external systems (e.g., Incredibuild, distcc-like tools) during the link step. This feature was contributed by PlayStation, who had offered it as a proprietary technology before upstreaming.

The traditional distributed ThinLTO is implemented in Bazel in buck2. **Bazel-style distribution** (build system orchestrated) uses a multi-step workflow:

```sh
# Compile to bitcode (made parallel by build system)
clang -c -O2 -flto=thin a.c b.c
# Thin link
clang -flto=thin -fuse-ld=lld -Wl,--thinlto-index-only=a.rsp,--thinlto-emit-imports-files -Wl,--thinlto-prefix-replace=';lto/' a.o b.o
# Backend compilation (distributed by build system) with dynamic dependencies
clang -c -O2 -fthinlto-index=lto/a.o.thinlto.bc a.o -o lto/a.o
clang -c -O2 -fthinlto-index=lto/b.o.thinlto.bc b.o -o lto/b.o
# Final native link
clang -fuse-ld=lld @a.rsp   # a.rsp contains lto/a.o and lto/b.o
```

The build system sees the index files from step 2 as outputs and schedules step 3 jobs across the build cluster. This requires a build system that handles **dynamic dependencies**—outputs of step 2 determine inputs to step 3.

**DTLTO** (linker orchestrated) integrates steps 2-4 into a single link invocation:

```sh
clang -flto=thin -c a.c b.c
clang -flto=thin -fuse-ld=lld -fthinlto-distributor=<distributor> *.o
```

LLD performs the thin-link internally, generates a JSON job description for each backend compilation, invokes the distributor process, waits for native objects, and links them. The distributor is responsible for farming out the compilations to remote machines.

DTLTO works with any build system but requires a separate distributor process that speaks its JSON protocol. DTLTO is essentially "ThinLTO distribution for projects that don't use Bazel".

## Pointer Field Protection

`R_AARCH64_PATCHINST` is a static relocation type used with Pointer Field Protection (PFP), which leverages Armv8.3-A Pointer Authentication (PAC) to protect pointer fields in structs.

Consider the following C++ code:

```cpp
struct cls {
  ~cls();
  long *ptr;
private:
  long *ptr2;
};

long *load(cls *c) { return c->ptr; }
void store(cls *c, long *ptr) { c->ptr = ptr; }
```

With Pointer Field Protection enabled, the compiler generates PAC instructions to sign and authenticate pointers:

```plaintext
load:
  ldr   x8, [x0]      // Load the PAC-signed pointer from c->ptr
  autda x8, x0        // Authenticate and strip the PAC, R_AARCH64_PATCHINST __pfp_ds__ZTS3cls.ptr
  mov   x0, x8
  ret

store:
  pacda x1, x0        // Sign ptr using c as a discriminator, R_AARCH64_PATCHINST __pfp_ds__ZTS3cls.ptr
  str   x1, [x0]
  ret
```

Each PAC instruction is associated with an `R_AARCH64_PATCHINST` relocation referencing a **deactivation symbol** (the `__pfp_ds_` prefix stands for "pointer field protection deactivation symbol"). By default, `__pfp_ds__ZTS3cls.ptr` is an undefined weak symbol in every relocatable file.

However, if the field's address escapes in any translation unit (e.g., someone takes `&c->ptr`), the compiler defines the deactivation symbol as an absolute symbol (ELF `SHN_ABS`). When the linker sees a defined deactivation symbol, it patches the PAC instruction to a NOP (`R_AARCH64_PATCHINST` acts as `R_AARCH64_ABS64` when the referenced symbol is defined), disabling the protection for that field. This is necessary because external code could modify the pointer without signing it, which would cause authentication failures.

The linker allows duplicate definitions of absolute symbols if the values are identical.

`R_AARCH64_FUNCINIT64` is a related static relocation type that produces an `R_AARCH64_IRELATIVE` dynamic relocation ([GNU indirect function](https://maskray.me/blog/2021-01-18-gnu-indirect-function)). It initializes function pointers in static data at load time by calling a resolver function that returns the PAC-signed address.

PFP is AArch64-specific because it relies on Pointer Authentication (PAC), a hardware feature introduced in Armv8.3-A. PAC provides dedicated instructions (`pacda`, `autda`, etc.) that cryptographically sign pointers using keys stored in system registers. x86-64 lacks an equivalent mechanism—Intel CET provides shadow stacks and indirect branch tracking for control-flow integrity, but cannot sign arbitrary data pointers stored in memory.

Takeaways:

- TU exposes a field's address, the linker disables protection for this field

  The implementation is usually lightweight.
- conditionally patches instructions to NOPs based on symbol resolution. This is a different paradigm from traditional "compute address, write it" relocations.

## RISC-V vendor relocations

RISC-V's openness encourages vendors to add custom instructions. Qualcomm has the uC extensions for their microcontrollers; CHERIoT adds capability-based security.

The RISC-V psABI adopted the vendor relocation system:

```plaintext
Relocation 0: R_RISCV_VENDOR      references symbol "QUALCOMM"
Relocation 1: R_RISCV_QC_ABS20_U  (vendor-specific type)
```

The `R_RISCV_VENDOR` marker identifies the vendor namespace via its symbol reference. The subsequent relocation uses a vendor-specific type number that only makes sense within that namespace. Different vendors can reuse the same type numbers without conflict.

In lld 22:

- #159987

  ). The implementation folds vendor namespace information into the upper bits of

  , allowing existing relocation processing code to work with minimal changes.
- #169273

  ), including Qualcomm and Andes relocation types. The patch landed without involving the regular lld/ELF reviewer pool. For changes that set architectural precedents, broader consensus should be sought before merging. I've

  commented

  on this.

The [RISC-V toolchain conventions](https://github.com/riscv-non-isa/riscv-toolchain-conventions) document the vendor relocation scheme.

There's a maintainability concern: accepting vendor-specific relocations into the core linker sets a precedent. RISC-V is uniquely fragmented compared to other LLVM backends-x86, AArch64, PowerPC, and others don't have nearly as many vendors adding custom instructions and relocations. This fragmentation is a direct consequence of RISC-V's open nature and extensibility, but it creates new challenges for upstream toolchain maintainers. Accumulated vendor-specific code could become a significant maintenance burden.

## GNU ld compatibility

Large corporate users of lld/ELF don't care about GNU ld compatibility. They add features for their own use cases and move on. I diligently coordinate with binutils maintainers and file feature requests when appropriate. When lld implements a new option or behavior, I often file corresponding GNU ld feature requests to keep the tools aligned.

This coordination work is largely invisible but essential for the broader toolchain ecosystem. Users benefit when they can switch between linkers without surprises.

---

Link: [lld 21 ELF changes](https://maskray.me/blog/2025-09-07-lld-21-elf-changes)
