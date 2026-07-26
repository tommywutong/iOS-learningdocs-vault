---
title: 'screenshotService(_:generatePDFRepresentationWithCompletion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscreenshotservicedelegate/screenshotservice(_:generatepdfrepresentationwithcompletion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscreenshotservicedelegate/screenshotservice(_:generatepdfrepresentationwithcompletion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreenshotservicedelegate/screenshotservice%28_%3Ageneratepdfrepresentationwithcompletion%3A%29.json'
content_hash: 'sha256:d10c9392ac9d141f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreenshotServiceDelegate](../uiscreenshotservicedelegate.md)

# screenshotService(_:generatePDFRepresentationWithCompletion:)

<sub>Instance Method</sub>

Generates a high-fidelity PDF version of the entire content in a given window scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func screenshotService(_ screenshotService: UIScreenshotService, generatePDFRepresentationWithCompletion completionHandler: @escaping (Data?, Int, CGRect) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func screenshotServiceGeneratePDFRepresentation(_ screenshotService: UIScreenshotService) async -> (Data?, Int, CGRect)
```

## Parameters

- `screenshotService` — A screenshot service object assigned to the relevant [UIWindowScene](../uiwindowscene.md) object. Use the window scene to retrieve the windows of your interface, and generate the PDF content from those windows.

- `completionHandler` — The completion handler block to call with the resulting PDF data. You must call this handler block at the end of your implementation, and pass in the relevant data. This handler block has no return value and takes the following parameters: - **PDFData** — The PDF data describing the content in the window scene. If you are unable to produce the PDF data, specify `nil`. - **indexOfCurrentPage** — The page index to associate with the PDF data. If your app separates its data into pages of content, use this parameter to specify the current page that the user is viewing. Page indexes are `0`-based, so the first page is at index `0`, the second at index `1`, and so on. Specify `0` if you don’t divide your app’s content into pages. - **rectInCurrentPage** — The bounds rectangle in the PDF content that approximates what the user was viewing in your window. Specify this rectangle in the PDF-coordinate space, which has an origin in the bottom-left corner of the content and a y-axis that extends upward. Specify [CGRectZero](../../coregraphics/cgrectzero.md) if you cannot provide the visible rectangle, or if you want the system to always display the PDF content starting at the top of the page.

## Discussion

When the user takes a screenshot of your app, UIKit calls this method to ask you for a PDF version of your content. In your implementation, create a high-fidelity PDF version of your content. At the end of your method, call `completionHandler` with the results.
