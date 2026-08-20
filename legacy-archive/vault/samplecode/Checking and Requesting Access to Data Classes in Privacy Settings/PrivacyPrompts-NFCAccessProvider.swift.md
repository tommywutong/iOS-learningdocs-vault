---
title: Checking and Requesting Access to Data Classes in Privacy Settings
apple_id: DTS40013410
resource_type: Sample Code
platform: iOS
topic: Security
technology: null
published: '2017-12-21'
source_url: https://developer.apple.com/library/archive/samplecode/PrivacyPrompts/Listings/PrivacyPrompts_NFCAccessProvider_swift.html
archived_at: '2026-07-18T03:19:34.550229Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Checking and Requesting Access to Data Classes in Privacy Settings](Checking%20and%20Requesting%20Access%20to%20Data%20Classes%20in%20Privacy%20Settings.md)


[Next](PrivacyPrompts-Supporting%20Files-Localizable.swift.md)[Previous](PrivacyPrompts-ContactsAccessProvider.swift.md)

# PrivacyPrompts/NFCAccessProvider.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Demonstrates API to requuest access to read NFC tags.
 */

import Foundation
import CoreNFC

class NFCAccessProvider: NSObject, PrivateDataAccessRequestProvider {

    var readerSession: NFCNDEFReaderSession?
    var requestAccessCompletionHandler: PrivacyActionRequestAccessHandler?

    func requestAccess(completionHandler: @escaping (PrivateDataRequestAccessResult) -> Void) {
        if NFCNDEFReaderSession.readingAvailable {
            requestAccessCompletionHandler = completionHandler

            /*
             Starting a NFC reader session will prompt the user with UI to scan a NFC tag.
             NFC reader access does not have an explicit authorization prompt, but still
             requires NFCReaderUsageDescription to be declared in the Info.plist file.
             If this string is not declared, the app will exit upon starting a NFC session.
            */
            readerSession = NFCNDEFReaderSession(delegate: self, queue: nil, invalidateAfterFirstRead: true)
            readerSession?.begin()
        } else {
            // NFC is not available on all iOS devices.
            completionHandler(PrivateDataRequestAccessResult(.unavailable))
        }
    }

    private func dispatchAccessResult(_ accessResult: PrivateDataRequestAccessResult) {
        DispatchQueue.main.async {
            if let completionHandler = self.requestAccessCompletionHandler {
                completionHandler(accessResult)

                // Breaks reference cycle so this object can deinit.
                self.requestAccessCompletionHandler = nil
            }
        }
    }
}

extension NFCAccessProvider: NFCNDEFReaderSessionDelegate {
    func readerSession(_ session: NFCNDEFReaderSession, didInvalidateWithError error: Error) {
        let result = PrivateDataRequestAccessResult(.unavailable,
                                                    error: error as NSError,
                                                    errorMessageKey: "NFC_SESSION_INVALIDATED_ERROR")
        dispatchAccessResult(result)
    }

    func readerSession(_ session: NFCNDEFReaderSession, didDetectNDEFs messages: [NFCNDEFMessage]) {
        dispatchAccessResult(PrivateDataRequestAccessResult(.granted))
    }
}
```

[Next](PrivacyPrompts-Supporting%20Files-Localizable.swift.md)[Previous](PrivacyPrompts-ContactsAccessProvider.swift.md)

