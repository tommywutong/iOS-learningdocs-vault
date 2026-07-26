---
title: Manual migrations
framework: Core Data
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/manual-migrations
source_url: 'https://developer.apple.com/documentation/coredata/manual-migrations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/manual-migrations.json'
content_hash: 'sha256:d0998447b8bc27fc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# Manual migrations

<sub>API Collection</sub>

Migrate elaborate data models with changes that go beyond the capabilities of both lightweight and staged migrations.

## Topics

### Entity Mapping

- [NSMigrationManager](nsmigrationmanager.md) — A migration manager instance that performs a migration of data from one persistent store to another using a given mapping model.
- [NSMappingModel](nsmappingmodel.md) — A model instance that specifies how to map a model from a source to a destination managed object model.
- [NSEntityMapping](nsentitymapping.md) — A mapping instance that specifies how to map an entity from a source to a destination managed object model.
- [NSEntityMigrationPolicy](nsentitymigrationpolicy.md) — A policy instance that customizes the migration process for an entity mapping.
- [NSEntityMappingType](nsentitymappingtype.md) — The types for mapping an entity between a source model and a destination model.
- [NSPropertyMapping](nspropertymapping.md) — A mapping instance that specifies in a model how to map from a property in a source entity to a property in a destination entity.

## See Also

### Data model migration

- [Migrating your data model automatically](migrating-your-data-model-automatically.md) — Enable lightweight migrations to keep your data model and the underlying data in a consistent state.
- [Staged migrations](staged-migrations.md) — Migrate complex data models containing changes that are incompatible with lightweight migrations.
