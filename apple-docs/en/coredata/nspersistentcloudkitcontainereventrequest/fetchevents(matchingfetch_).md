---
title: 'fetchEvents(matchingFetch:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentcloudkitcontainereventrequest/fetchevents(matchingfetch:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainereventrequest/fetchevents(matchingfetch:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainereventrequest/fetchevents%28matchingfetch%3A%29.json'
content_hash: 'sha256:d2333505740af2ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentCloudKitContainerEventRequest](../nspersistentcloudkitcontainereventrequest.md)

# fetchEvents(matchingFetch:)

<sub>Type Method</sub>

Creates a fetch request for events that match a specified fetch request from a persistent CloudKit container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func fetchEvents(matchingFetch fetchRequest: NSFetchRequest<any NSFetchRequestResult>) -> Self
```

## Parameters

- `fetchRequest` — A fetch request to identify matching events.

## Return Value

A request object that fetches persistent CloudKit container events by executing in a managed object context.

## See Also

### Fetching Events

- [+ fetchEventsAfterDate:](<fetchevents(after_)-5izg7.md>) — Creates a fetch request for events after a specified date from a persistent CloudKit container.
- [+ fetchEventsAfterEvent:](<fetchevents(after_)-3yfp.md>) — Creates a fetch request for events that occur after a specified event from a persistent CloudKit container.
- [+ fetchRequestForEvents](<fetchforevents().md>) — Creates a fetch request for all events in a persistent CloudKit container.
- [resultType](resulttype.md) — The type of result that the request returns.
