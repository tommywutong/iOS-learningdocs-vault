---
title: Open source at F8 2019
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2019/05/01/open-source/f8-open-source/'
original_language: en
published: 2019-05-01
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3fd42bf6a1d504d0'
translated: false
---

> 原文：[Open source at F8 2019](https://engineering.fb.com/2019/05/01/open-source/f8-open-source/)　·　Meta Engineering — iOS

At F8, Facebook’s annual conference, we open-sourced tools and frameworks that simplify machine learning experimentation and optimization, speed up test execution times, and help solve memory-related performance issues. See the full list below, and click through to get started with our latest releases.

## [Ax](https://ax.dev)

Ax is an accessible, general-purpose adaptive experimentation platform for managing, deploying, and automating experiments. The platform makes it easier for developers to optimize their products and infrastructure by leveraging recent advances provided by BoTorch, our library for Bayesian optimization (BO) research. Ax also lowers the barrier for BO, multiarmed bandit, and other complicated experimentation techniques, allowing researchers to take their ideas from research to production.  
 [Read the Facebook AI blog post on Ax and BoTorch for more information.](https://ai.facebook.com/blog/open-sourcing-ax-and-botorch-new-ai-tools-for-adaptive-experimentation)  
 [Start using Ax.](https://ax.dev)

## [BoTorch](https://botorch.org)

BoTorch is a library for Bayesian optimization (BO) research, built on PyTorch. BoTorch significantly boosts developer efficiency by combining a modular design and use of Monte Carlo-based acquisition functions with PyTorch’s auto-differentiation feature. BoTorch’s ability to integrate with any PyTorch model allows for a high degree of flexibility and facilitates research at the intersection of BO and deep learning.  
 [Read the Facebook AI blog post on Ax and BoTorch for more information.](https://ai.facebook.com/blog/open-sourcing-ax-and-botorch-new-ai-tools-for-adaptive-experimentation)  
 [Start using BoTorch.](https://botorch.org)

## [Idb](https://github.com/facebook/FBSimulatorControl)

The iOS development bridge (idb) is a command line interface for automating iOS simulators and devices. The provided API of simple primitives makes it easy to build complex worfklows. Idb also has a client-server architecture that makes it easier to distribute work between a fleet of machines so that automation on iOS can be distributed amongst a fleet of machines.  
 [Start using idb.](https://github.com/facebook/FBSimulatorControl)

## [Memscout](https://github.com/facebookincubator/memscout)

Memscout is an analysis tool that’s a companion to the jemalloc memory allocator (the default memory allocator used across Facebook’s infrastructure services). Memscout interprets the raw data in a jemalloc stats file (JSON format) for a running process and highlights relevant metrics. It scouts out allocator inefficiencies and provides insights into memory allocation patterns of the process, and then presents a breakdown of statistics that can be used to quickly diagnose memory-related performance issues.  
 [Start using Memscout.](https://github.com/facebookincubator/memscout)

## [Mvfst](https://github.com/facebookincubator/mvfst)

Mvfst is an implementation of the QUIC transport protocol. The goal of mvfst is to build the most flexible, performant transport protocol that applications could adapt for use cases on the internet and within the data center. Features include stream multiplexing as a transport feature, 0-RTT connection establishment, better loss recovery, security built in from the ground up, and flexible congestion control.  
 [Start using mvfst.](https://github.com/facebookincubator/mvfst)

For a full recap of everything announced at F8, see the keynotes from [Day 1](https://engineering.fb.com/developer-tools/f8-2019-day-1/). For more about all our open source projects, visit [Facebook Open Source](https://opensource.facebook.com/).
