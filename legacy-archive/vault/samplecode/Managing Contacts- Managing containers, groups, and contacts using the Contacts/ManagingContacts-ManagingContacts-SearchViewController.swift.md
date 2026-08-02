---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_SearchViewController_swift.html
archived_at: '2026-07-18T03:14:29.087361Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-MGCHelperClass.swift.md)[Previous](ManagingContacts-ManagingContacts-TabBarViewController.swift.md)

# ManagingContacts/ManagingContacts/SearchViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A table view controller that allows you to search contacts by 
                name (first name, last name, and organization name).
 */

import Contacts
import UIKit

class SearchViewController: UITableViewController, UISearchResultsUpdating {
    // MARK: - Types

    fileprivate struct MainStoryboard {
        struct TableViewCellIdentifiers {
            static let cellIdentifier = "cellID"
            static let cellSubtitleIdentifier = "cellSubtitleID"
        }
    }


    // MARK: - Properties

    /// Stores all contacts available in the contact store.
    fileprivate var allContacts = [CNContact]()

    // Stores contacts matching the search string.
    fileprivate var filteredContacts = [CNContact]()
    fileprivate var searchController: UISearchController!

    /**
        - returns: Boolean value that determines whether to show a subtitle cell.\
                   true if the contact is a person and the matching name was found 
                   in its associated organization name rather than in its name. 
                   Also true if the contact is an organization and the matching 
                   name was found in its associated formatted name. false, 
                   otherwise.
    */
    fileprivate var shouldShowSubtitleCell: Bool = false

    var data: [CNContact] = [CNContact]() {
        didSet {
            filteredContacts = data
            allContacts = data
            tableView.reloadData()
        }
    }


    // MARK: - View Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()

        // Create the search controller.
        searchController = UISearchController(searchResultsController: nil)
        searchController.searchResultsUpdater = self

        // Make sure the that the search bar is visible within the navigation bar.
        searchController.searchBar.sizeToFit()

        // Include the search controller's search bar in the table header view.
        tableView.tableHeaderView = searchController.searchBar
        searchController.dimsBackgroundDuringPresentation = false
        definesPresentationContext = true
    }


    // MARK: - UITableViewDataSource

    override func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return filteredContacts.count
    }


    // MARK: - UITableViewDelegate    

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        var cell: UITableViewCell
        let contact = filteredContacts[indexPath.row]
        var name = String()

        if let searchString = searchController.searchBar.text, !(searchString.isEmpty) {
            /* CNContact's predicateForContactsMatchingName looks thru the first 
               name, last name, and organization name fields of a contact. In 
               some cases, Contacts may find the searched name in the organization 
               name of a contact, which is a person or in the first name and
               last name of a contact, which is an organization.
               Display a subtitle cell if the contact is a person and its first 
               name and last name do not contain the search string.
            */
            if contact.isPerson && !(contact.formattedName.localizedCaseInsensitiveContains(searchString)) {

                name = contact.organizationName
                shouldShowSubtitleCell = true
            }
            // Display a subtitle cell if the contact is an organization and its name does not contain the searchString
            else if !contact.isPerson && !(contact.organizationName.localizedCaseInsensitiveContains(searchString)) {

                name = (contact.familyName.localizedCaseInsensitiveContains(searchString)) ? contact.familyName : contact.givenName
                shouldShowSubtitleCell = true
            }
        }

        if shouldShowSubtitleCell {

            cell = tableView.dequeueReusableCell(withIdentifier: MainStoryboard.TableViewCellIdentifiers.cellSubtitleIdentifier, for: indexPath)
            // Display the name of the contact.
            cell.textLabel!.text = (contact.isPerson) ? contact.formattedName : contact.organizationName

            // Display the contact's associated field containing the search string.
            cell.detailTextLabel!.text = name
        }
        else {

            cell = tableView.dequeueReusableCell(withIdentifier: MainStoryboard.TableViewCellIdentifiers.cellIdentifier, for: indexPath)
            cell.textLabel!.text = (contact.isPerson) ? contact.formattedName : contact.organizationName
       }
       return cell
    }


    // MARK: -  UISearchResultsUpdating

    func updateSearchResults(for searchController: UISearchController) {
        let searchString = searchController.searchBar.text

        /*
            Show all contacts if the user did not enter anything. Show the 
            contacts matching the search string otherwise.
        */
        if searchString!.isEmpty {

            filteredContacts = allContacts
            tableView.reloadData()
        }
        else {
            MGCContactStore.sharedInstance.fetchContacts(with: searchString!, completion: ({(contacts: [CNContact]) in
                self.filteredContacts = contacts
                self.tableView.reloadData()
            }))
        }
    }


    // MARK: - Memory Management

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
}
```

[Next](ManagingContacts-ManagingContacts-MGCHelperClass.swift.md)[Previous](ManagingContacts-ManagingContacts-TabBarViewController.swift.md)

