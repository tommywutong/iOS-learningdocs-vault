---
title: Determining system capabilities
framework: Kernel
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/kernel/1387446-sysctlbyname/determining_system_capabilities
source_url: 'https://developer.apple.com/documentation/kernel/1387446-sysctlbyname/determining_system_capabilities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/kernel/1387446-sysctlbyname/determining_system_capabilities.json'
content_hash: 'sha256:ada9d755f4089e88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Kernel](../../kernel.md) · [sys](../sys.md) · [sysctlbyname](../1387446-sysctlbyname.md)

# Determining system capabilities

<sub>Article</sub>

Interrogate the system for processor, cache, and topology information.

## Overview

Obtain information about parameters related to processor availability, cache size, and performance-level characteristics on the system by using the [sysctlbyname](../1387446-sysctlbyname.md) function. These parameters provide details about your system that can aid in tuning performance. For example, you can obtain the count of the highest-performing processor cores to spawn a worker thread for each core. Or you can determine the size of the L2 cache and the number of processor cores that share it to perform software cache-blocking optimization.

### Determine processor characteristics

The system enables a processor core when it’s powered on and available for thread scheduling. Each logical processor core executes a software thread that the operating system manages. On systems where the number of logical processor cores exceeds the number of physical processor cores, two or more logical processor cores share a physical core through simultaneous multithreading (SMT). The following parameters provide processor availability information about the system on chip (SoC):

- **`hw.activecpu`** — The number of enabled logical processor cores in the SoC. This is an alias of `hw.logicalcpu`.
- **`hw.ncpu`** — The number of logical processor cores in the SoC. This is an alias of `hw.logicalcpu_max`.
- **`hw.logicalcpu`** — The number of enabled logical processor cores in the SoC. This is an alias of `hw.activecpu`.
- **`hw.logicalcpu_max`** — The number of logical processor cores in the SoC. This is an alias of `hw.ncpu`.
- **`hw.physicalcpu`** — The number of enabled physical processor cores in the SoC.
- **`hw.physicalcpu_max`** — The number of physical processor cores in the SoC.

### Determine system topology

The following parameters provide processor core performance-level information. First, determine the number of types of processor cores with `hw.nperflevels`. Then, for each of the parameters, replace _N_ with a number between `0` and the number of performance levels minus one. Lower values of _N_ indicate higher-performance core types.

- **`hw.nperflevels`** — The number of types of general purpose processor cores in the SoC.
- **`hw.perflevel`_N_`.cpusperl2`** — For processor cores of performance level_ N_, the number of cores that share an L2 cache.
- **`hw.perflevel`_N_`.cpusperl3`** — For processor cores of performance level_ N_, the number of cores that share an L3 cache.
- **`hw.perflevel`_N_`.l1dcachesize`** — For processor cores of performance level _N_, the size in bytes of the L1 data cache.
- **`hw.perflevel`_N_`.l1icachesize`** — For processor cores of performance level _N_, the size in bytes of the L1 instruction cache.
- **`hw.perflevel`_N_`.l2cachesize`** — For processor cores of performance level _N_, the size in bytes of the L2 cache.
- **`hw.perflevel`_N_`.l3cachesize `** — For processor cores of performance level _N_, the size in bytes of the L3 cache.
- **`hw.perflevel`_N_`.logicalcpu`** — For processor cores of performance level _N_, the number of enabled logical cores in the SoC.
- **`hw.perflevel`_N_`.logicalcpu_max`** — For processor cores of performance level _N_, the number of logical cores in the SoC.
- **`hw.perflevel`_N_`.physicalcpu`** — For processor cores of performance level _N_, the number of enabled physical cores in the SoC.
- **`hw.perflevel`_N_`.physicalcpu_max`** — For processor cores of performance level _N_, the number of physical cores in the SoC.

Querying the following parameters is equivalent to querying the per-performance-level information for the least performant core. For example, `hw.l1dcachesize` is equivalent to `hw.perflevel[`_N_`].l1dcachesize`, where _N_ is `hw.nperflevels` minus one.

- **`hw.l1dcachesize`** — The size in bytes of the L1 data cache.
- **`hw.l1icachesize`** — The size in bytes of the L1 instruction cache.
- **`hw.l2cachesize`** — The size in bytes of the L2 cache.
- **`hw.l3cachesize`** — The size in bytes of the L3 cache.

### Determine memory sizes

The following parameters provide cache line, memory, and page size information:

- **`hw.cachelinesize`** — The size in bytes of the system cache line.
- **`hw.memsize`** — The size in bytes of dynamic RAM.
- **`hw.pagesize`** — The size in bytes of a virtual memory page.

## See Also

### Parameters

- [Determining Instruction Set Characteristics](determining_instruction_set_characteristics.md) — Interrogate the system for details about the instruction set.
