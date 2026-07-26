---
title: 'batchUpdateRequestWithEntityName:'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsbatchupdaterequest/batchupdaterequestwithentityname:'
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchupdaterequest/batchupdaterequestwithentityname:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchupdaterequest/batchupdaterequestwithentityname%3A.json'
content_hash: 'sha256:165d911f031ac068'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchUpdateRequest](../nsbatchupdaterequest.md)

# batchUpdateRequestWithEntityName:

<sub>Type Method</sub>

Creates a batch-update request for a named managed entity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) batchUpdateRequestWithEntityName:(NSString *) entityName;
```

## Parameters

- `entityName` — The name of the managed entity to update data for.

## Return Value

A batch-update request.

## See Also

### Creating a Request

- [- initWithEntity:](<init(entity_).md>) — Creates a batch-update request for a managed entity.
- [- initWithEntityName:](<init(entityname_).md>) — Creates a batch-update request for a named managed entity.
