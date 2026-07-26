---
title: Running tests serially or in parallel
framework: Swift Testing
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/testing/parallelization
source_url: 'https://developer.apple.com/documentation/testing/parallelization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/testing/parallelization.json'
content_hash: 'sha256:6cd139735a8d626f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Testing](../testing.md) · [Traits](traits.md)

# Running tests serially or in parallel

<sub>Article</sub>

Control whether tests run serially or in parallel.

## Overview

By default, tests run in parallel with respect to each other. Parallelization is accomplished by the testing library using task groups, and tests generally all run in the same process. The number of tests that run concurrently is controlled by the Swift runtime.

## Disabling parallelization

Parallelization can be disabled on a per-function or per-suite basis using the [serialized](trait/serialized.md) trait:

```swift
@Test(.serialized, arguments: Food.allCases) func prepare(food: Food) {
  // This function will be invoked serially, once per food, because it has the
  // .serialized trait.
}

@Suite(.serialized) struct FoodTruckTests {
  @Test(arguments: Condiment.allCases) func refill(condiment: Condiment) {
    // This function will be invoked serially, once per condiment, because the
    // containing suite has the .serialized trait.
  }

  @Test func startEngine() async throws {
    // This function will not run while refill(condiment:) is running. One test
    // must end before the other will start.
  }
}
```

When added to a parameterized test function, this trait causes that test to run its cases serially instead of in parallel. When applied to a non-parameterized test function, this trait has no effect. When applied to a test suite, this trait causes that suite to run its contained test functions and sub-suites serially instead of in parallel.

This trait is recursively applied: if it is applied to a suite, any parameterized tests or test suites contained in that suite are also serialized (as are any tests contained in those suites, and so on.)

This trait doesn’t affect the execution of a test relative to its peers or to unrelated tests. This trait has no effect if test parallelization is globally disabled (by, for example, passing `--no-parallel` to the `swift test` command.)

## See Also

### Running tests serially or in parallel

- [serialized](trait/serialized.md) — A trait that serializes the test to which it is applied.
