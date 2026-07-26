---
title: 'activityViewControllerLinkMetadata(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiactivityitemsource/activityviewcontrollerlinkmetadata(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsource/activityviewcontrollerlinkmetadata(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsource/activityviewcontrollerlinkmetadata%28_%3A%29.json'
content_hash: 'sha256:05feaf7ed44714df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityItemSource](../uiactivityitemsource.md)

# activityViewControllerLinkMetadata(_:)

<sub>Instance Method</sub>

Returns metadata to display in the preview header of the share sheet.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func activityViewControllerLinkMetadata(_ activityViewController: UIActivityViewController) -> LPLinkMetadata?
```

## Parameters

- `activityViewController` — The [UIActivityViewController](../uiactivityviewcontroller.md) object requesting information about the item that the user wants to share.

## Return Value

The [LPLinkMetadata](../../linkpresentation/lplinkmetadata.md) object that contains the metadata about a URL, including its title, icon, images, and video.

## Discussion

Using the [Link Presentation](../../linkpresentation.md) framework, you can display rich previews of web links inside your app. For instance, if your app already has a database of links, with titles and images that weren’t fetched by [LPMetadataProvider](../../linkpresentation/lpmetadataprovider.md), you don’t have to fetch new metadata from the internet. Use this method instead and avoid downloading it again.

In your implementation, create an [LPLinkMetadata](../../linkpresentation/lplinkmetadata.md) object, and fill in at least the [originalURL](../../linkpresentation/lplinkmetadata/originalurl.md) and [url](../../linkpresentation/lplinkmetadata/url.md) fields, plus whatever additional information you have.

```swift
func activityViewControllerLinkMetadata(_: UIActivityViewController) -> LPLinkMetadata? {
    let metadata = LPLinkMetadata()
    metadata.originalURL = URL(string: "https://www.example.com/apple-pie")
    metadata.url = metadata.originalURL
    metadata.title = "The Greatest Apple Pie In The World"
    metadata.imageProvider = NSItemProvider.init(contentsOf:
        Bundle.main.url(forResource: "apple-pie", withExtension: "jpg"))
    return metadata
}
```

To learn more about presenting rich links and accelerating the share sheet, see [Link Presentation](../../linkpresentation.md) and [LPMetadataProvider](../../linkpresentation/lpmetadataprovider.md), or watch the WWDC 2019 session [262: Embedding and Sharing Visually Rich Links](https://developer.apple.com/videos/play/wwdc2019/262/).
