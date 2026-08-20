---
title: 'TCPTransports: Using Various Apple APIs to Run a TCP Connection'
apple_id: TP40017680
resource_type: Sample Code
platform: iOS
topic: null
technology: NetworkExtension
published: '2018-05-10'
source_url: https://developer.apple.com/library/archive/samplecode/TCPTransports/Listings/App_iOS_EndpointPicker_swift.html
archived_at: '2026-07-18T03:25:59.920107Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCPTransports: Using Various Apple APIs to Run a TCP Connection](TCPTransports-%20Using%20Various%20Apple%20APIs%20to%20Run%20a%20TCP%20Connection.md)


[Next](Tests-TestServer.swift.md)[Previous](App-iOS-ConversationViewController.swift.md)

# App-iOS/EndpointPicker.swift

```swift
/*
    Copyright (C) 2018 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Runs the main view, letting the user configure an endpoint to connect to.
 */

import UIKit

/// Runs the main view, letting the user configure an endpoint to connect to.
/// This no nothing about networking as such, it’s just a view that lets you
/// input some networking parameters.  The delegate is responsible for checking
/// those parameters and actually starting a conversation based on them.

class EndpointPicker : UITableViewController, UITextFieldDelegate {

    typealias Delegate = EndpointPickerDelegate

    weak var delegate: Delegate? = nil

    /// Set this before presenting the view controller to configure the initial display.
    /// Read this in delegate callbacks to get the current configuration.

    var endpoint: Endpoint = .empty

    // MARK: - View Controller Methods

    override func viewDidLoad() {
        super.viewDidLoad()
        self.hostNameField.text = self.endpoint.hostName
        self.portField.text = self.portNumberFormatter.string(from: self.endpoint.port as NSNumber)
        self.useTLSSwitch = UISwitch()
        self.useTLSSwitch.addTarget(self, action: #selector(didChange(useTLSSwitch:)), for: .valueChanged)
        self.useTLSCell.accessoryView = self.useTLSSwitch
        self.connectTextColor = self.connectCell.textLabel!.textColor!
        self.enableConnectCell()
        self.cell(for: self.endpoint.transport).accessoryType = .checkmark
    }

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "startConnection" {
            self.delegate?.prepareStartConnection(segue: segue, endpointPicker: self)
        } else {
            super.prepare(for: segue, sender: sender)
        }
    }

    // MARK: - Table View Controller Callbacks

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {

        // Deselect by default.

        var shouldDeselect = true
        defer {
            tableView.deselectRow(at: indexPath, animated: true)
        }

        switch Section(rawValue: indexPath.section)! {
        case .general:
            if indexPath == tableView.indexPath(for: self.connectCell) && self.connectCell.selectionStyle == .default {
                if let message = self.delegate?.check(endpointPicker: self) {
                    self.displayConfigurationUnsupportedAlert(message: message)
                } else {
                    self.performSegue(withIdentifier: "startConnection", sender: self)
                    // The table view deselects as we come back on screen.
                    shouldDeselect = false
                }
            }
        case .transports:
            self.cell(for: self.endpoint.transport).accessoryType = .none
            self.endpoint.transport = Endpoint.Transport(rawValue: indexPath.row)!
            self.cell(for: self.endpoint.transport).accessoryType = .checkmark
        }
    }

    // MARK: - Utilities

    /// An enumeration that describes the layout of the table view.
    ///
    /// - general: The first section holds our general UI. Item in this section
    ///   are accessed via various IBOutlets.
    /// - transports: The second section holds our transports. Items in this
    ///   section are accessed by using the raw value of the `Transport`
    ///   enumeration to index the `transportCells` IBOutletCollection.

    private enum Section : Int {
        case general
        case transports
    }

    /// Used for rendering and parsing port numbers.

    private var portNumberFormatter: NumberFormatter = {
        let nf = NumberFormatter()
        nf.numberStyle = .decimal
        nf.usesGroupingSeparator = false
        return nf
    }()

    /// Returns the cell for a given transport.

    private func cell(for transport: Endpoint.Transport) -> UITableViewCell {
        return self.transportCells[transport.rawValue]
    }

    /// Called when the UI changes to enable or disable the Connect cell.

    private func enableConnectCell() {
        let isEnabled = !self.endpoint.hostName.isEmpty && (1...65535).contains(self.endpoint.port)
        self.connectCell.selectionStyle = isEnabled ? .default : .none
        self.connectCell.textLabel!.textColor = isEnabled ? self.connectTextColor : .gray
    }

    /// Displays a "Configuration Unsupported" alert with the supplied message.

    private func displayConfigurationUnsupportedAlert(message: String) {
        let alert = UIAlertController(
            title: NSLocalizedString("_Unsupported_Configuration_", comment: "Title for alert view."),
            message: message,
            preferredStyle: .alert
        )
        alert.addAction(UIAlertAction(title: NSLocalizedString("_OK_", comment: "Default button in alert view."), style: .default, handler: { (_) in
            self.dismiss(animated: true, completion: nil)
        }))
        self.present(alert, animated: true, completion: nil)
    }

    // MARK: - Outlets, Actions and Text Field Delegate Callbacks

    @IBAction private func didChange(hostNameField: UITextField) {
        let newText = (self.hostNameField.text ?? "").trimmingCharacters(in: .whitespacesAndNewlines)
        self.endpoint.hostName = newText
        self.enableConnectCell()
    }

    @IBAction private func didChange(portField: UITextField) {
        let newText = self.portField.text ?? ""
        let newPort = self.portNumberFormatter.number(from: newText)?.intValue ?? 0
        self.endpoint.port = newPort
        self.enableConnectCell()
    }

    @IBAction private func didChange(useTLSSwitch: UISwitch) {
        self.endpoint.useTLS = self.useTLSSwitch.isOn
    }

    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        return true
    }

    @IBOutlet private var hostNameField: UITextField!
    @IBOutlet private var portField: UITextField!
    @IBOutlet private var useTLSCell: UITableViewCell!
    private var useTLSSwitch: UISwitch!
    @IBOutlet private var connectCell: UITableViewCell!
    private var connectTextColor: UIColor!
    @IBOutlet private var transportCells: [UITableViewCell]!
}

/// Delegate protocol for `EndpointPicker`.

protocol EndpointPickerDelegate : AnyObject {

    /// Called to check whether a particular endpoint configuration is viable.
    ///
    /// - Parameters:
    ///   - endpoint: The endpoint configuration in question.
    ///   - endpointPicker: The sender.
    /// - Returns: `nil` if the endpoint is viable; a localised message to
    ///   display otherwise.

    func check(endpointPicker: EndpointPicker) -> String?

    /// Called to prepare `startConnection` segue.
    ///
    /// - Parameters:
    ///   - segue: The `segue`, which holds the destination view controller.
    ///   - endpointPicker: The sender.

    func prepareStartConnection(segue: UIStoryboardSegue, endpointPicker: EndpointPicker)
}
```

[Next](Tests-TestServer.swift.md)[Previous](App-iOS-ConversationViewController.swift.md)

