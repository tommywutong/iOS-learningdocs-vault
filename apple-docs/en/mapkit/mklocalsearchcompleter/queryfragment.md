---
title: queryFragment
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, macOS 10.11.4+, tvOS 9.2+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearchcompleter/queryfragment
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/queryfragment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearchcompleter/queryfragment.json'
content_hash: 'sha256:86a6d894b4dc36eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalSearchCompleter](../mklocalsearchcompleter.md)

# queryFragment

<sub>Instance Property</sub>

The search string that you want completions for.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var queryFragment: String { get set }
```

## Discussion

Assigning a string to this property initiates a search based on that string. The completer object waits a short amount of time before initiating new searches. This delay gives you enough time to update the search string based on typed input from the user. For example, if you’re using a text field to manage the input from the user, use the [textField(_:shouldChangeCharactersIn:replacementString:)](<../../uikit/uitextfielddelegate/textfield(__shouldchangecharactersin_replacementstring_).md>) method of the text field’s delegate to update the value of this property, as the following example shows:

```objc
- (BOOL)textField:(UITextField *)textField shouldChangeCharactersInRange:(NSRange)range
         replacementString:(NSString *)string {
    self.completer.queryFragment = textField.text;
 
    return YES;
}
```

## See Also

### Specifying the query attributes

- [addressFilter](addressfilter.md) — A filter that lists which address options to include or exclude in search results.
- [region](region.md) — The region that defines the geographic scope of the search.
- [regionPriority](regionpriority.md) — A value that indicates the importance of the configured region.
- [resultTypes](resulttypes.md) — The types of search completions to include.
- [pointOfInterestFilter](pointofinterestfilter.md) — A filter that lists point of interest categories to include or exclude in the search.
- [filterType](filtertype-swift.property.md) — The filter options for the search results. _(deprecated)_
- [FilterType](filtertype-swift.enum.md) — Constants indicating the types of search completions to return. _(deprecated)_
- [ResultType](resulttype.md) — Options that indicate types of search completions.
