---
title: 'LoopHealth: Using health documents and Activity rings in HealthKit and HealthKitUI'
apple_id: TP40017553
resource_type: Sample Code
platform: watchOS|iOS
topic: null
technology: null
published: '2016-12-02'
source_url: https://developer.apple.com/library/archive/samplecode/LoopHealth/Listings/LoopHealth_RecordsListTableViewController_swift.html
archived_at: '2026-07-18T03:13:50.158541Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LoopHealth: Using health documents and Activity rings in HealthKit and HealthKitUI](LoopHealth-%20Using%20health%20documents%20and%20Activity%20rings%20in%20HealthKit%20and%20HealthKit.md)


[Next](LoopHealth-AppDelegate.swift.md)[Previous](README.md.md)

# LoopHealth/RecordsListTableViewController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The second of two main view controllers for the LoopHealth app.
 */

import UIKit
import HealthKit

/**
    View controller for the second tab of the LoopHealth app. Displays user's
    health records; the user can tap on a record entry to view its content.
 */
class RecordsListTableViewController: UITableViewController, HealthStoreContainer {

    // MARK: Properties

    static let cellIdentifier = "recordCellIdentifier"

    /**
        The `HKHealthStore` that this view controller should use to query data.
        It is expected that this property is set by the presenter of this view
        controller. For this sample, this is the application delegate.
    */
    var healthStore: HKHealthStore!

    var healthDocumentSamples = [HKCDADocumentSample]()

    // MARK: UIViewController

    override func viewDidLoad() {
        super.viewDidLoad()

        // Get CDA type to read and write.
        guard let cdaDocumentType = HKObjectType.documentType(forIdentifier: .CDA) else { return }
        let typesToRead = Set<HKObjectType>([cdaDocumentType])
        let typesToWrite = Set<HKSampleType>([cdaDocumentType])

        healthStore.requestAuthorization(toShare: typesToWrite, read: typesToRead) { success, error in
            self.queryForHealthDocuments()
        }
    }

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        super.prepare(for: segue, sender: sender)

        // Get the selected `HKCDADocumentSample`.
        if let selectedIndex = tableView.indexPathForSelectedRow {
            let documentSample = healthDocumentSamples[selectedIndex.row]

            // Pass the `HKCDADocumentSample` to the presented view controller.
            segue.destination.enumerateHierarchy { viewController in
                guard let detailViewController = viewController as? RecordsDetailViewController else { return }
                detailViewController.healthDocumentSample = documentSample
                detailViewController.healthStore = healthStore
            }
        }
    }

    // MARK: UITableViewDataSource

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return healthDocumentSamples.count
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        guard let cell = tableView.dequeueReusableCell(withIdentifier: RecordsListTableViewController.cellIdentifier) else { fatalError("Unable to dequeue cell from tableview") }

        let healthDocumentSample = healthDocumentSamples[indexPath.row]
        cell.textLabel?.text = healthDocumentSample.document?.title
        cell.detailTextLabel?.text = healthDocumentSample.document?.custodianName

        return cell
    }

    // MARK: IBActions

    @IBAction func addCDAToHealthKit() {
        /*
            Load CDA from `Bundle`, transform into `Data` object, then create
            sample and save into HealthKit.
         */
        if let cdaURL = Bundle.main.url(forResource: "AGooseff", withExtension: "xml") {
            let cdaData = try! Data(contentsOf: cdaURL)
            let date = Date()
            let cdaSample = try! HKCDADocumentSample(data: cdaData, start: date, end: date, metadata: nil)

            healthStore.save(cdaSample) { success, error in
                DispatchQueue.main.async {
                    // Present an alert.
                    let alertController = UIAlertController(title: "Success", message: "Successfully added health document to HeakthKit", preferredStyle: .alert)
                    let okAction = UIAlertAction(title: "Ok", style: .default, handler: nil)
                    alertController.addAction(okAction)
                    self.present(alertController, animated: true, completion: nil)

                    // Requery for updated health documents to update the table view.
                    self.queryForHealthDocuments()
                }
            }
        }
    }

    // MARK: Private methods

    private func queryForHealthDocuments() {
        healthDocumentSamples.removeAll()
        guard let documentType = HKObjectType.documentType(forIdentifier: .CDA) else { return }

        // Query for our samples without document data.
        let healthDocumentsQuery = HKDocumentQuery(documentType: documentType, predicate:nil, limit: 10, sortDescriptors: nil, includeDocumentData: false) { query, samples, done, error in
            guard let samples = samples as? [HKCDADocumentSample], !samples.isEmpty else { return }

            DispatchQueue.main.async {
                /*
                    Samples can come back one by one, append to our current
                    list of samples then reload table.
                 */
                self.healthDocumentSamples.append(contentsOf: samples)
                self.tableView.reloadData()
            }
        }

        healthStore.execute(healthDocumentsQuery)
    }
}
```

[Next](LoopHealth-AppDelegate.swift.md)[Previous](README.md.md)

