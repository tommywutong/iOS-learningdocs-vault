---
title: ZoomingPDFViewer
apple_id: DTS40010281
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: CoreGraphics
published: '2017-04-27'
source_url: https://developer.apple.com/library/archive/samplecode/ZoomingPDFViewer/Listings/ZoomingPDFViewerSwift_ZoomingPDFViewerUITests_ZoomingPDFViewerUITests_swift.html
archived_at: '2026-07-18T03:28:45.195477Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZoomingPDFViewer](ZoomingPDFViewer.md)


[Next](ZoomingPDFViewerSwift-ZoomingPDFViewerTests-ZoomingPDFViewerTests.swift.md)[Previous](ZoomingPDFViewerCocoa-ZoomingPDFViewer-main.m.md)

# ZoomingPDFViewerSwift/ZoomingPDFViewerUITests/ZoomingPDFViewerUITests.swift

```swift
//
//  ZoomingPDFViewerUITests.swift
//  ZoomingPDFViewerUITests
//
//  Created by john on 4/6/17.
//  Copyright © 2017 Apple. All rights reserved.
//

import XCTest

class ZoomingPDFViewerUITests: XCTestCase {

    override func setUp() {
        super.setUp()

        // Put setup code here. This method is called before the invocation of each test method in the class.

        // In UI tests it is usually best to stop immediately when a failure occurs.
        continueAfterFailure = false
        // UI tests must launch the application that they test. Doing this in setup will make sure it happens for each test method.
        XCUIApplication().launch()

        // In UI tests it’s important to set the initial state - such as interface orientation - required for your tests before they run. The setUp method is a good place to do this.
    }

    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
        super.tearDown()
    }

    func testExample() {
        // Use recording to get started writing UI tests.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
    }

}
```

[Next](ZoomingPDFViewerSwift-ZoomingPDFViewerTests-ZoomingPDFViewerTests.swift.md)[Previous](ZoomingPDFViewerCocoa-ZoomingPDFViewer-main.m.md)

