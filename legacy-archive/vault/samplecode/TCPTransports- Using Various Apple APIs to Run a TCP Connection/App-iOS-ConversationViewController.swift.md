---
title: 'TCPTransports: Using Various Apple APIs to Run a TCP Connection'
apple_id: TP40017680
resource_type: Sample Code
platform: iOS
topic: null
technology: NetworkExtension
published: '2018-05-10'
source_url: https://developer.apple.com/library/archive/samplecode/TCPTransports/Listings/App_iOS_ConversationViewController_swift.html
archived_at: '2026-07-18T03:25:59.829061Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCPTransports: Using Various Apple APIs to Run a TCP Connection](TCPTransports-%20Using%20Various%20Apple%20APIs%20to%20Run%20a%20TCP%20Connection.md)


[Next](App-iOS-EndpointPicker.swift.md)[Previous](App-iOS-ActiveConversation.swift.md)

# App-iOS/ConversationViewController.swift

```swift
/*
    Copyright (C) 2018 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Displays a conversation in a table view, with support for sending messages.
 */

import UIKit

/// This class displays a conversation in table view, along with a UI that lets
/// the user send a message on an online conversation.  It is entirely separated
/// from the networking stack, allow it to be used (and tested!) without any
/// networking.  The only requirement are:
///
/// * Someone must set the `conversation` property when the conversation
///   changes.
///
/// * Someone should act as the delegate for the sake of both closing the
///   conversation and sending messages.

class ConversationViewController : UITableViewController {

    /// The conversation being displayed.  Changes to this will update the UI.

    var conversation: Conversation = .empty {
        didSet {
            self.title = self.conversation.localizedName

            guard self.isViewLoaded else { return }

            // If the update has just added new messages we insert those at the
            // end in order to get a cleaner animation.  Otherwise we just
            // reload everything from scratch.

            let newMessageCount = self.conversation.messages.count
            let oldMessageCount = oldValue.messages.count
            if oldMessageCount != 0 && newMessageCount > oldMessageCount {
                let newIndexPaths = (oldMessageCount..<newMessageCount).map { IndexPath(row: $0, section: Sections.messages.rawValue) }
                self.tableView.insertRows(at: newIndexPaths, with: .automatic)
            } else {
                self.tableView.reloadSections(IndexSet([Sections.messages.rawValue]), with: .automatic)
            }

            // IMPORTANT: We have to do this reload after dealing with any
            // insertions in the `.messages` section because the reload can
            // trigger a call to our data source methods and those will return
            // info about the new value not the old value.

            if self.conversation.state != oldValue.state {
                self.tableView.reloadSections([Sections.status.rawValue], with: .automatic)
            }
        }
    }

    typealias Delegate = ConversationViewControllerDelegate

    weak var delegate: Delegate? = nil

    // MARK: - Table View Callbacks

    override func numberOfSections(in tableView: UITableView) -> Int {
        return Sections.status.rawValue + 1
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        switch Sections(rawValue: section)! {
        case .messages: return max(self.conversation.messages.count, 1)
        case .status: return 1
        }
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        switch (Sections(rawValue: indexPath.section)!, indexPath.row, self.conversation.state) {
        case (.messages, 0, _) where self.conversation.messages.isEmpty:
            return tableView.dequeueReusableCell(withIdentifier: "none", for: indexPath)
        case (.messages, _, _):
            let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath) as! MessageCell
            cell.message = self.conversation.messages[indexPath.row]
            return cell
        case (.status, 0, .online):
            let cell = tableView.dequeueReusableCell(withIdentifier: "compose", for: indexPath) as! ComposeCell
            cell.parent = self
            return cell
        case (.status, 0, .offline(let localizedStatus)):
            let cell = tableView.dequeueReusableCell(withIdentifier: "offline", for: indexPath)
            cell.textLabel!.text = localizedStatus
            return cell
        default:
            fatalError()
        }
    }

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        self.tableView.deselectRow(at: indexPath, animated: true)
    }

    // MARK: - Internals

    private enum Sections : Int {
        case messages
        case status
    }

    /// This is called by `ComposeCell` when there’s a message to send.  I could have made
    /// a `ComposeCell.Delegate` to handle this, but the reality is that `ComposeCell` and
    /// this class are super tightly bound already so I don’t feel so bad about having it
    /// call us like this.
    ///
    /// - Parameter message: The message to send.

    func sendMessage(message: String) {
        self.delegate?.send(message: message, conversationViewController: self)
    }

    /// Wired up to the Done button.

    @IBAction private func doneAction(_ sender: Any) {
        self.delegate?.close(conversationViewController: self)
    }
}

/// Delegate protocol for `ConversationViewController`.

protocol ConversationViewControllerDelegate : AnyObject {

    /// Called when the user wants to send a message.  The delegate is expected to
    /// send the message _and_ reflect it back in `conversation.messages`.
    ///
    /// - Parameters:
    ///   - message: The message to send.
    ///   - conversationViewController: The sender.

    func send(message: String, conversationViewController: ConversationViewController)

    /// Called when the user indicates that they want to close the conversation.
    ///
    /// - Parameter conversationViewController: The sender.

    func close(conversationViewController: ConversationViewController)
}

/// A cell for the `.messages` section of the table view.  This has the smarts
/// necessary to render a message in some reasonably pleasing way.
///
/// - note: I’d prefer if this were private but that causes a runtime failure..

class MessageCell : UITableViewCell {

    var message: Message? = nil {
        didSet {
            guard let message = self.message else {
                self.messageLabel.text = "_N/A_"  // not localised because it should never be seen
                return
            }
            let format: String
            switch message.direction {
            case .incoming: format = NSLocalizedString("_<-_%@_", comment: "Format for incoming message in the messages view.")
            case .outgoing: format = NSLocalizedString("_->_%@_", comment: "Format for outgoing message in the messages view.")
            }
            self.messageLabel.text = String(format: format, message.text)
        }
    }

    @IBOutlet private var messageLabel: UILabel!
}

/// A cell for the `.status` secton of the conversation table view.  This runs a
/// text field in which the user can enter messages.
///
/// - note: I’d prefer if this were private but that causes a runtime failure..

class ComposeCell : UITableViewCell, UITextFieldDelegate {

    /// A reference to the parent view controller.  When a message is reading to
    /// go this cell calls that view controller’s `sendMessage(message:)`
    /// method. I could have used a delegate here but deemed that wasn’t
    /// necessary as this class is already tightly couple to the view
    /// controller.

    weak var parent: ConversationViewController? = nil

    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        if let message = self.messageField.text, !message.isEmpty, let parent = self.parent {
            self.messageField.text = ""
            parent.sendMessage(message: message)
        }
        return false
    }

    @IBOutlet private var messageField: UITextField!
}
```

[Next](App-iOS-EndpointPicker.swift.md)[Previous](App-iOS-ActiveConversation.swift.md)

