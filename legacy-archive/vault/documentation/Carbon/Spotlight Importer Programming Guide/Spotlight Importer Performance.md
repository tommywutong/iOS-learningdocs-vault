---
title: Spotlight Importer Programming Guide
apple_id: TP40001267
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreServices
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MDImporters/Concepts/Performance.html
archived_at: '2026-07-15T05:23:20.061469Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Spotlight Importer Programming Guide](About%20Spotlight%20Importers.md)


[Next](Troubleshooting%20Spotlight%20Importers.md)[Previous](Writing%20a%20Spotlight%20Importer.md)

# Spotlight Importer Performance

A Spotlight importer is called upon as files are created, copied, and modified, so performance is crucial. Importers should be able to extract metadata from files quickly and with minimal effort.

Avoid burying metadata deep inside a file, especially if finding that metadata would be computationally intensive later. If required for performance improvements, define your file format so that relevant information at a fixed or easily accessed location in the file.

It is also vital that your importer does not leak memory, because this can also contribute to performance problems. Be sure to profile and test your importer using Instruments and the other provided profiling software to ensure it is as fast as possible.

[Next](Troubleshooting%20Spotlight%20Importers.md)[Previous](Writing%20a%20Spotlight%20Importer.md)

