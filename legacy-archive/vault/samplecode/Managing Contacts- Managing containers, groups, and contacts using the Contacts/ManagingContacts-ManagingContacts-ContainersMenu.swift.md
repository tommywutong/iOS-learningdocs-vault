---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_ContainersMenu_swift.html
archived_at: '2026-07-18T03:14:27.864329Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-MenuViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-MGCMenuSectionFeature.swift.md)

# ManagingContacts/ManagingContacts/ContainersMenu.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A MenuViewController subclass that displays and manages navigation
                menu features in the Containers tab. 
                Source view controller for the fetchAllContainers, 
                fetchContactsPerContainer, performFetchContactsPerContainer, and
                performFetchGroupsPerContainer segues.
*/

import UIKit
import Contacts

class ContainersMenu: MenuViewController {
    // MARK: - Handle refreshTabNotification

    override func handleRefreshTabNotification(_ notification: Notification) {
        let tabBarNotification = notification.object as! TabBarViewController
        // Update the data model for this tab.
        navigationMenuContent = tabBarNotification.containersMenu
        tableView.reloadData()
    }


    // MARK: - Convenience Method

    /// Create a data model object that organize containers per type.
    fileprivate func buildDataModel(with containers: [CNContainer]) -> [MGCModel] {
        var result = [MGCModel]()

        // Parse the containers array for Local, Exchange, and CardDAV containers.
        let local = menuContactStoreUtilities.filter(containers, for: .local)
        let exchange = menuContactStoreUtilities.filter(containers, for: .exchange)
        let carddav = menuContactStoreUtilities.filter(containers, for: .cardDAV)


        // Only use the ones that have data.
        if local.count > 0 {
            result.append(MGCModel(tab: MGCAppConfiguration.Content.containers, content: local, category: MGCAppConfiguration.MainStoryboard.TableHeaderSection.Containers.local))
        }

        if exchange.count > 0 {
            result.append(MGCModel(tab: MGCAppConfiguration.Content.containers, content: exchange, category: MGCAppConfiguration.MainStoryboard.TableHeaderSection.Containers.exchange))
        }

        if carddav.count > 0 {
            result.append(MGCModel(tab: MGCAppConfiguration.Content.containers, content: carddav, category: MGCAppConfiguration.MainStoryboard.TableHeaderSection.Containers.carddav))
        }

        return result
    }


    // MARK: - Navigation

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        let item = navigationMenuContent[tableView.indexPathForSelectedRow!.section].section[tableView.indexPathForSelectedRow!.row]

        // Implement the "Fetch default container" and "Fetch all containers" features.
        if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Containers.fetchDefaultContainer || segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Containers.fetchAllContainers {
            let groupedViewController = segue.destination as! GroupedViewController

            if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Containers.fetchDefaultContainer {

                groupedViewController.title = item.title

                // Fetch the default container.
                MGCContactStore.sharedInstance.fetchContainer(with: MGCContactStore.sharedInstance.defaultContainerID, completion: ({(container: CNContainer?) in
                    if let defaultContainer = container {

                        let header = defaultContainer.nameMatchingContainerType
                        groupedViewController.data = [MGCModel(tab: MGCAppConfiguration.Content.containers, content: [defaultContainer], category: header)]
                    }
                }))
            }
            else if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Containers.fetchAllContainers {

                groupedViewController.title = item.title

                // Fetch all containers.
                MGCContactStore.sharedInstance.fetchContainers({(containers: [CNContainer]) in
                    if containers.count > 0 {

                        let allContainers = self.buildDataModel(with: containers)
                        groupedViewController.data = allContainers
                    }})
            }
        }
            // Implement the "Fetch groups per container" and "Fetch contacts per container" features.
        else if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Containers.performFetchGroupsPerContainer || segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Containers.performFetchContactsPerContainer {

            let mainViewController = segue.destination as! MainViewController
            mainViewController.title = item.title

            if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Containers.performFetchGroupsPerContainer {

                // Fetch all containers.
                MGCContactStore.sharedInstance.fetchContainers({(containers: [CNContainer]) in
                    if containers.count > 0 {

                        // Exchange containers do not have groups. As such, we are only local and CardDav ones.
                        var data = self.menuContactStoreUtilities.filter(containers, for: .local)
                        data += self.menuContactStoreUtilities.filter(containers, for: .cardDAV)

                        mainViewController.data = [MGCModel(tab: MGCAppConfiguration.Content.containers, content: data, segue: item.segue)]
                    }})
            }
            else if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Containers.performFetchContactsPerContainer {

                // Fetch all containers.
                MGCContactStore.sharedInstance.fetchContainers({(containers: [CNContainer]) in
                    if containers.count > 0 {
                        var data = self.menuContactStoreUtilities.filter(containers, for: .local)
                        data += self.menuContactStoreUtilities.filter(containers, for: .exchange)
                        data += self.menuContactStoreUtilities.filter(containers, for: .cardDAV)

                        mainViewController.data = [MGCModel(tab: MGCAppConfiguration.Content.containers, content: data, segue: item.segue)]
                    }})
            }
        }
    }
}
```

[Next](ManagingContacts-ManagingContacts-MenuViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-MGCMenuSectionFeature.swift.md)

