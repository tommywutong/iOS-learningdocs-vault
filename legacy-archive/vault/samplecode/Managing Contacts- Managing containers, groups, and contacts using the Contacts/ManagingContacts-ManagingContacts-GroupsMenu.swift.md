---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_GroupsMenu_swift.html
archived_at: '2026-07-18T03:14:28.093787Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-GroupedViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-AppDelegate.swift.md)

# ManagingContacts/ManagingContacts/GroupsMenu.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A MenuViewController subclass that displays and manages navigation 
                 menu features in the Groups tab.
                 Implements the unwind saveGroup segue to create and save a group to
                 a given container.
                 Source view conroller for the fetchAllGroups, 
                 performFetchContactsPerGroup, addGroup, deleteGroup, 
                 performAddContactToGroup, and performRemoveContactFromGroup segues.
*/

import UIKit
import Contacts

class GroupsMenu: MenuViewController {
   // MARK: - Handle refreshTabNotification

    override func handleRefreshTabNotification(_ notification: Notification) {
        let tabBarNotification = notification.object as! TabBarViewController

        // Update the data model for this tab.
        navigationMenuContent = tabBarNotification.groupsMenu
        tableView.reloadData()
    }


    // MARK: - UITableViewDataSource

    override func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        return navigationMenuContent[section].title
    }


    // MARK: - Convenience Method

    fileprivate func handleAddGroup(with segue: UIStoryboardSegue, with title: String) {
        let navigationController = segue.destination as! UINavigationController
        let addGroupViewController = navigationController.topViewController as! AddGroupViewController

        addGroupViewController.title = title
        addGroupViewController.data = [MGCModel(tab: MGCAppConfiguration.Content.groups,
                                           category: MGCAppConfiguration.MainStoryboard.TableHeaderSection.Groups.addGroup)]

        /* Exchange accounts don't support groups. Fetch local and cardDAV 
           containers that can be chosen to contain a group.
        */
        MGCContactStore.sharedInstance.fetchContainers({(containers: [CNContainer]) in
            if containers.count > 0 {

                var dataModel = [CNContainer]()

                let carddav = self.menuContactStoreUtilities.filter(containers, for: .cardDAV)
                if carddav.count > 0 {
                    dataModel.append(contentsOf: carddav)
                }

                let local = self.menuContactStoreUtilities.filter(containers, for: .local)
                if local.count > 0 {
                    dataModel.append(contentsOf: local)
                }

                addGroupViewController.data.append(MGCModel(tab: MGCAppConfiguration.Content.groups,
                                                        content: dataModel,
                                                       category: MGCAppConfiguration.MainStoryboard.TableHeaderSection.Groups.selectContainer))
            }
        })
    }


    // MARK: - Navigation

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        let item = navigationMenuContent[tableView.indexPathForSelectedRow!.section].section[tableView.indexPathForSelectedRow!.row]

        // Implement the "Fetch all groups" feature.
        if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.fetchAllGroups {

            let detailViewController = segue.destination as! DetailViewController
            detailViewController.title = item.title

             MGCContactStore.sharedInstance.fetchGroups({(groups: [CNGroup]) in
                if groups.count > 0 {
                    detailViewController.data = [MGCModel(tab: MGCAppConfiguration.Content.containers,
                                                      content: groups,
                                                     category: MGCAppConfiguration.Content.groups)]
                }
             })
        }
        // Implement the "Fetch contacts per group" feature.
        else if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.performFetchContactsPerGroup {

            let mainViewController = segue.destination as! MainViewController
            mainViewController.title = item.title

            MGCContactStore.sharedInstance.fetchGroups({(groups: [CNGroup]) in
                if groups.count > 0 {
                    mainViewController.data = [MGCModel(tab: MGCAppConfiguration.Content.groups,
                                                    content: groups,
                                                      segue: item.segue)]
                }
            })
        }
        // Implement the "Add a group" feature.
        else if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.addGroup {
            handleAddGroup(with: segue, with: item.title)
        }
        // Implement the "Update a group" feature.
        else if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.performUpdateGroup {

            let mainViewController = segue.destination as! MainViewController
            mainViewController.title = item.title

            MGCContactStore.sharedInstance.fetchGroups({(groups: [CNGroup]) in
                if groups.count > 0 {
                    mainViewController.data = [MGCModel(tab: MGCAppConfiguration.Content.groups,
                                                    content: groups,
                                                      segue: item.segue)]
                }
            })
        }
        // Implement the "Delete a group" feature.
        else if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.deleteGroup {

            let editViewController = segue.destination as! EditViewController
            editViewController.title = item.title

            MGCContactStore.sharedInstance.fetchGroups({(groups: [CNGroup]) in
                if groups.count > 0 {
                    editViewController.data = [MGCModel(tab: MGCAppConfiguration.Content.groups,
                                                    content: groups,
                                                      segue: item.segue)]
                }
            })
        }
        // Implement the "Add a contact to a group" feature.
        else if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.performAddContactToGroup {

            let plainViewController = segue.destination as! PlainViewController
            plainViewController.title = item.title

            MGCContactStore.sharedInstance.fetchGroups({(groups: [CNGroup]) in
                if groups.count > 0 {
                    plainViewController.data = [MGCModel(tab: MGCAppConfiguration.Content.groups,
                                                     content: groups,
                                                       segue: item.segue)]
                }
            })
        }
        // Implement the "Remove contact from a group" feature.
        else if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.performRemoveContactFromGroup {

            let mainViewController = segue.destination as! MainViewController
            mainViewController.title = item.title

            MGCContactStore.sharedInstance.fetchGroups({(groups: [CNGroup]) in
                if groups.count > 0 {
                    mainViewController.data = [MGCModel(tab: MGCAppConfiguration.Content.groups,
                                                    content: groups,
                                                      segue: item.segue)]
                }
            })
        }
    }


    // MARK: - Actions

    @IBAction func cancel(_ sender: UIStoryboardSegue) {
        dismiss(animated: true, completion: nil)
    }

    /// Attempt to create and save a group to a given container.
    @IBAction func saveGroup(_ sender: UIStoryboardSegue) {
        if  let addGroupViewController = sender.source as? AddGroupViewController, let name = addGroupViewController.group, let containerID = addGroupViewController.containerID {
            MGCContactStore.sharedInstance.save(name, toContainerWithIdentifier: containerID)
        }
    }
}
```

[Next](ManagingContacts-ManagingContacts-GroupedViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-AppDelegate.swift.md)

