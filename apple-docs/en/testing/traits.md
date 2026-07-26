---
title: Traits
framework: Swift Testing
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/testing/traits
source_url: 'https://developer.apple.com/documentation/testing/traits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/testing/traits.json'
content_hash: 'sha256:b5c3c4ec093e5078'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Testing](../testing.md)

# Traits

<sub>API Collection</sub>

Annotate test functions and suites, and customize their behavior.

## Overview

Pass built-in traits to test functions or suite types to comment, categorize, classify, and modify the runtime behavior of test suites and test functions. Implement the [TestTrait](testtrait.md), and [SuiteTrait](suitetrait.md) protocols to create your own types that customize the behavior of your tests.

## Topics

### Customizing runtime behaviors

- [Enabling and disabling tests](enablinganddisabling.md) — Conditionally enable or disable individual tests before they run.
- [Limiting the running time of tests](limitingexecutiontime.md) — Set limits on how long a test can run for until it fails.
- [enabled(if:_:sourceLocation:)](<trait/enabled(if___sourcelocation_).md>) — Constructs a condition trait that disables a test if it returns `false`.
- [enabled(_:sourceLocation:_:)](<trait/enabled(__sourcelocation___).md>) — Constructs a condition trait that disables a test if it returns `false`.
- [disabled(_:sourceLocation:)](<trait/disabled(__sourcelocation_).md>) — Constructs a condition trait that disables a test unconditionally.
- [disabled(if:_:sourceLocation:)](<trait/disabled(if___sourcelocation_).md>) — Constructs a condition trait that disables a test if its value is true.
- [disabled(_:sourceLocation:_:)](<trait/disabled(__sourcelocation___).md>) — Constructs a condition trait that disables a test if its value is true.
- [timeLimit(_:)](<trait/timelimit(__).md>) — Construct a time limit trait that causes a test to time out if it runs for too long.

### Running tests serially or in parallel

- [Running tests serially or in parallel](parallelization.md) — Control whether tests run serially or in parallel.
- [serialized](trait/serialized.md) — A trait that serializes the test to which it is applied.

### Annotating tests

- [Adding tags to tests](addingtags.md) — Use tags to provide semantic information for organization, filtering, and customizing appearances.
- [Adding comments to tests](addingcomments.md) — Add comments to provide useful information about tests.
- [Associating bugs with tests](associatingbugs.md) — Associate bugs uncovered or verified by tests.
- [Interpreting bug identifiers](bugidentifiers.md) — Examine how the testing library interprets bug identifiers provided by developers.
- [Tag()](<tag().md>) — Declare a tag that can be applied to a test function or test suite.
- [bug(_:_:)](<trait/bug(____).md>) — Constructs a bug to track with a test.
- [bug(_:id:_:)](<trait/bug(__id___)-10yf5.md>) — Constructs a bug to track with a test.
- [bug(_:id:_:)](<trait/bug(__id___)-3vtpl.md>) — Constructs a bug to track with a test.

### Handling issues

- [compactMapIssues(_:)](<trait/compactmapissues(__).md>) — Constructs an trait that transforms issues recorded by a test.
- [filterIssues(_:)](<trait/filterissues(__).md>) — Constructs a trait that filters issues recorded by a test.

### Creating custom traits

- [Trait](trait.md) — A protocol describing traits that can be added to a test function or to a test suite.
- [TestTrait](testtrait.md) — A protocol describing a trait that you can add to a test function.
- [SuiteTrait](suitetrait.md) — A protocol describing a trait that you can add to a test suite.
- [TestScoping](testscoping.md) — A protocol that tells the test runner to run custom code before or after it runs a test suite or test function.

### Supporting types

- [Bug](bug.md) — A type that represents a bug report tracked by a test.
- [Comment](comment.md) — A type that represents a comment related to a test.
- [ConditionTrait](conditiontrait.md) — A type that defines a condition which must be satisfied for the testing library to enable a test.
- [IssueHandlingTrait](issuehandlingtrait.md) — A type that allows transforming or filtering the issues recorded by a test.
- [ParallelizationTrait](parallelizationtrait.md) — A type that defines whether the testing library runs this test serially or in parallel.
- [Tag](tag.md) — A type representing a tag that can be applied to a test.
- [List](tag/list.md) — A type representing one or more tags applied to a test.
- [TimeLimitTrait](timelimittrait.md) — A type that defines a time limit to apply to a test.
