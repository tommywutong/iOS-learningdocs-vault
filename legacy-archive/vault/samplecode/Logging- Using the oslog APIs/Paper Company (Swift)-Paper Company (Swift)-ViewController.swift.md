---
title: 'Logging: Using the os_log APIs'
apple_id: TP40017510
resource_type: Sample Code
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Logging/Listings/Paper_Company__Swift__Paper_Company__Swift__ViewController_swift.html
archived_at: '2026-07-18T03:13:47.809086Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Logging: Using the os_log APIs](Logging-%20Using%20the%20oslog%20APIs.md)


[Next](Paper%20Company%20%28Swift%29-Paper%20Company%20%28Swift%29-AppDelegate.swift.md)[Previous](Paper%20Company-ReadMe.md.md)

# Paper Company (Swift)/Paper Company (Swift)/ViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A simple interface with a few buttons to trigger logging events. Demonstrates the Activity APIs.
 */

import UIKit
import os.log

public class ViewController: UIViewController {
    // MARK: Properties

    static let ui_log = OSLog(subsystem: "com.example.apple-samplecode.Paper-Company-Swift", category: "UI")

    private(set) public var company: PaperCompany!

    // MARK: Interface Builder outlets

    @IBOutlet weak var companyNameLabel: UILabel!
    @IBOutlet weak var treeButton: UIButton!
    @IBOutlet weak var truckButton: UIButton!
    @IBOutlet weak var paperButton: UIButton!

    // MARK: UIViewController

    override public func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        company = PaperCompany(name: companyNameLabel.text!)
        os_log("Created company named %@", log: ViewController.ui_log, company.companyName)
        updateButtonCounts()
    }

    // MARK: Interface Builder actions.

    /// Chop down a tree to turn into a log.
    @IBAction private func treeButtonTapped(sender: UIButton) {
        os_log("Cutting down trees to turn them into logs", log: ViewController.ui_log, type: .info)
        os_log("Sender: %@", log: ViewController.ui_log, type: .debug, sender)
        company.chopDownTree()
        updateButtonCounts()
    }

    /// Send logs to the paper mill to be turned into paper.
    @IBAction private func truckButtonTapped(sender: UIButton) {
        os_log("Taking logs to the paper mill", log: ViewController.ui_log, type: .info)
        os_log("Sender: %@", log: ViewController.ui_log, type: .debug, sender)
        company.makePaper()
        updateButtonCounts()
    }

    /// This does nothing. Paper is useless in our modern world.
    @IBAction private func paperButtonTapped(sender: UIButton) {
        os_log("Paper is useless in our modern world!", log: ViewController.ui_log, type: .info)
        os_log("Sender: %@", log: ViewController.ui_log, type: .debug, sender)
        updateButtonCounts()
    }

    /// Simulate a crash.
    @IBAction func bombButtonTapped(sender: AnyObject) {
        /*
            Use `error` when something goes wrong in your app, and use `fault` when
        something goes wrong involving another process. Both `os_log_error` and
        `os_log_fault` do extra work to make sure the relevant information is
        preserved, so only call them when something actually goes wrong.
        */
        os_log("B-b-b-b-b-b-b-bomb!", log: ViewController.ui_log, type: .error)

        // Don't try this at home, kids!
        company = nil
        company!.chopDownTree()
    }

    // MARK: Convenience

    private func updateButtonCounts() {
        os_log("Updating button counts", log: ViewController.ui_log)
        treeButton.setTitle("🌲 x\(company.livingTrees)", for: [])
        truckButton.setTitle("🚚 x\(company.logs)", for: [])
        paperButton.setTitle("📄 x\(company.papers)", for: [])
    }
}
```

[Next](Paper%20Company%20%28Swift%29-Paper%20Company%20%28Swift%29-AppDelegate.swift.md)[Previous](Paper%20Company-ReadMe.md.md)

