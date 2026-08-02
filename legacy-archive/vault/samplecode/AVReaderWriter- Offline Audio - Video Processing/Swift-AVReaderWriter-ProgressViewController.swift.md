---
title: 'AVReaderWriter: Offline Audio / Video Processing'
apple_id: DTS40011124
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/ReaderWriter/Listings/Swift_AVReaderWriter_ProgressViewController_swift.html
archived_at: '2026-07-18T03:21:58.605610Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVReaderWriter: Offline Audio / Video Processing](AVReaderWriter-%20Offline%20Audio%20-%20Video%20Processing.md)


[Next](Swift-AVReaderWriter-CyanifyOperation.swift.md)[Previous](Swift-AVReaderWriter-AppDelegate.swift.md)

# Swift/AVReaderWriter/ProgressViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Defines the view controller for the progress scene.
*/

import UIKit

class ProgressViewController: UIViewController {
    // MARK: Properties

    var sourceURL: NSURL?

    var outputURL: NSURL?

    lazy var operationQueue: NSOperationQueue = {
        let operationQueue = NSOperationQueue()

        operationQueue.name = "com.example.apple-samplecode.progressviewcontroller.operationQueue"

        return operationQueue
    }()

    weak var cyanifier: CyanifyOperation?

    static let finishingSegueName = "finishing"

    static let cancelSegueName = "cancel"

    // MARK: IBActions

    @IBAction func cancel() {
        cyanifier?.cancel()
    }

    // MARK: View Controller

    override func viewDidAppear(animated: Bool) {
        super.viewDidAppear(animated)

        guard let outputURL = outputURL, sourceURL = sourceURL else {
            fatalError("`outputURL` and `sourceURL` should not be nil when \(#function) is called.")
        }

        // Create video processing operation and add it to our operation queue.

        let cyanifier = CyanifyOperation(sourceURL: sourceURL, outputURL: outputURL)

        cyanifier.completionBlock = { [weak cyanifier] in
            /*
                Operation must still be alive when it invokes its completion handler.
                It also must have set a non-nil result by the time it finishes.
            */
            let result = cyanifier!.result!

            dispatch_async(dispatch_get_main_queue()) {
                self.cyanificationDidFinish(result)
            }
        }

        operationQueue.addOperation(cyanifier)

        self.cyanifier = cyanifier
    }

    private func cyanificationDidFinish(result: CyanifyOperation.Result) {
        switch result {
            case .Success:
                performSegueWithIdentifier(ProgressViewController.finishingSegueName, sender: self)

            case .Failure(let error):
                presentError(error as NSError)

            case .Cancellation:
                performSegueWithIdentifier(ProgressViewController.cancelSegueName, sender: self)
        }
    }

    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if segue.identifier == ProgressViewController.finishingSegueName {
            let nextViewController = segue.destinationViewController as! ResultViewController

            nextViewController.outputURL = outputURL
        }
    }

    /// Present an `NSError` to the user.
    func presentError(error: NSError) {
        let failureTitle = error.localizedDescription

        let failureMessage = error.localizedRecoverySuggestion ?? error.localizedFailureReason

        let alertController = UIAlertController(title: failureTitle, message: failureMessage, preferredStyle: .Alert)

        let alertAction = UIAlertAction(title: "OK", style: .Default) { _ in
            self.performSegueWithIdentifier("error", sender: self)
        }

        alertController.addAction(alertAction)

        presentViewController(alertController, animated: true, completion: nil)
    }
}
```

[Next](Swift-AVReaderWriter-CyanifyOperation.swift.md)[Previous](Swift-AVReaderWriter-AppDelegate.swift.md)

