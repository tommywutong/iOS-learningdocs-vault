---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_TabBarViewController_swift.html
archived_at: '2026-07-18T03:14:29.157736Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-SearchViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-MGCContactStore.swift.md)

# ManagingContacts/ManagingContacts/TabBarViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Tab bar view controller that manages the Containers, Contacts, and 
                Groups view controllers.
                It checks access to the Contacts application. It listens and handles 
                ContactStore refresh data notifications.
                Fetches Contacts' contacts and groups, then use the result of these 
                operations to provide and manage the UI of its child view controllers.
*/

import UIKit
import Contacts

class TabBarViewController: UITabBarController {
    // MARK: - Types

    fileprivate struct MenuPlist {
        static let name = "Menu"
        static let fileExtension = "plist"
    }


    // MARK: - Properties

    /// Contains navigation menu for the Contacts tab.
    var contactsMenu = [MGCMenuSection]()

    /// Contains navigation menu for the Containers tab.
    var containersMenu = [MGCMenuSection]()

    /// Contains navigation menu for the Groups tab.
    var groupsMenu = [MGCMenuSection]()

    /// Used to parse the Menu plist file.
    fileprivate var parsingUtilities: MGCParsingUtilities!

    /** 
        The Contacts app can have one or more containers. In the event that it 
        only contains one, we use isExchangeAccount to determine whether this 
        container is an Exchange account.
   */
    fileprivate var isExchangeAccount = false

    /// - returns: true if Contacts contains one or more groups and false, otherwise.
    fileprivate var didFindGroups = false

    /// - returns: true if Contacts contains one or more contacts and false, otherwise.
    fileprivate var didFindContacts = false

    /** 
        The Contacts app can have one or more containers with one defined as the 
        default by the user. You cannot add groups to an Exchange account.
        Furthermore, some features such as adding a contact to a group require 
        the existence of both a contact and a group. As a result, ManagingContacts
        will always implement the following features: Fetch the default container,
        Fetch all containers, and Add a contact. It will disable features such
        as "Add a group" and "Fetch groups per container" when the default container 
        is an Exchange account.
    */
    fileprivate var defaultFeatures = [MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Containers.fetchDefaultContainer,
                                       MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Containers.fetchAllContainers,
                                       MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Contacts.addContact]

    /// These features require the existence of groups, which are unsupported by Exchange accounts.
    fileprivate var groupsFeatures = [MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.addGroup,
                                      MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Containers.performFetchGroupsPerContainer]

    // MARK: - View Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()
        // Register for ContactStore's storeDidChange notifications.
        NotificationCenter.default.addObserver(self, selector: #selector(TabBarViewController.handleStoreDidChangeNotification(_:)), name: NSNotification.Name(rawValue: MGCAppConfiguration.MGCNotifications.storeDidChange), object: MGCContactStore.sharedInstance)
        privacyAccessStatus()
    }

    // MARK: -  Update UI

    /// Provides the default navigation menu.
    fileprivate func configureMenuNavigation() {
        parsingUtilities = MGCParsingUtilities(name: MenuPlist.name, fileExtension: MenuPlist.fileExtension)

        if parsingUtilities.resourceWasFound() {

            // Get the initial menu for the Contacts, Containers, and Groups tabs.
            if let tempContacts = parsingUtilities.parse(for: MGCAppConfiguration.Content.contacts),
                let tempContainers = parsingUtilities.parse(for: MGCAppConfiguration.Content.containers),
                let tempGroups = parsingUtilities.parse(for: MGCAppConfiguration.Content.groups) {

                contactsMenu = tempContacts
                containersMenu = tempContainers
                groupsMenu = tempGroups
            }
        }
        else {
                DispatchQueue.main.async {
                    let message = MGCAppConfiguration.Messages.resourceNotFound+"\(MenuPlist.name).\(MenuPlist.fileExtension)."

                    let alert = MGCHelperClass.alert(with: NSLocalizedString(MGCAppConfiguration.Messages.status, comment: MGCAppConfiguration.MainStoryboard.Cells.emptyString),
                                                  message: NSLocalizedString(message, comment: MGCAppConfiguration.MainStoryboard.Cells.emptyString))

                    self.present(alert, animated: true, completion: nil)
            }
        }
    }

    /// Update each tab's data model.
    fileprivate func refreshTabsDataModel(with availableContacts: Bool, with availableGroups: Bool, exchangeAccount: Bool) {
        containersMenu = toggleAccessoryControls(in: MGCAppConfiguration.Content.containers,
                                            content: containersMenu,
                                               with: availableContacts,
                                               with: availableGroups,
                                               with: exchangeAccount)


        groupsMenu = toggleAccessoryControls(in: MGCAppConfiguration.Content.groups,
                                        content: groupsMenu,
                                           with: availableContacts,
                                           with: availableGroups,
                                           with: exchangeAccount)


        contactsMenu = toggleAccessoryControls(in: MGCAppConfiguration.Content.contacts,
                                          content: contactsMenu,
                                             with: availableContacts,
                                             with: availableGroups,
                                             with: exchangeAccount)
    }

    /// Enable or disable the accessory controls for each feature in the navigation menu.
    fileprivate func toggleAccessoryControls(in tab: String, content: [MGCMenuSection], with availableContacts: Bool, with availableGroups: Bool, with exchangeAccount: Bool) -> [MGCMenuSection] {
        content.flatMap({menuSection in menuSection.section}).forEach({item in

            if (defaultFeatures.contains(item.segue.main) == true) {
                item.enabled = true
            }
            else if (groupsFeatures.contains(item.segue.main) == true) {
                item.enabled = !exchangeAccount
            }
            else if (tab == MGCAppConfiguration.Content.groups) {
                item.enabled = (exchangeAccount) ? false : availableGroups
            }
            else if tab == MGCAppConfiguration.Content.contacts {
                item.enabled = availableContacts
            }
        })
        return content
    }


    // MARK: - Disable UI

    /**
        Called when the user has denied or restricted access to Contacts. 
        Disable the UI as a result.
    */
    fileprivate func disableUI() {
        if let firstViewController = viewControllers?.first {
            firstViewController.view.isUserInteractionEnabled = false
        }

        tabBar.items!.forEach { item in
            item.isEnabled = false
        }
    }


    // MARK: - Check Contacts Privacy Access

    /** 
        Check the authorization status of our application for Contacts.
        Disable the UI if access was denied.
    */
    fileprivate func privacyAccessStatus() {
       MGCContactStore.sharedInstance.checkContactsAccess({(accessGranted: Bool) in
            if accessGranted {

                self.configureMenuNavigation()
                self.fetchContainersContactsAndGroups()
            }
            else {

                DispatchQueue.main.async {
                    /* Access was denied or restricted, let's disable all tabs 
                       and present an alert to the user.
                    */
                    self.disableUI()
                    let alert = MGCHelperClass.alert(with: NSLocalizedString(MGCAppConfiguration.Messages.status, comment: MGCAppConfiguration.MainStoryboard.Cells.emptyString),
                                                  message: NSLocalizedString(MGCAppConfiguration.Messages.accessDenied, comment: MGCAppConfiguration.MainStoryboard.Cells.emptyString))

                    self.present(alert, animated: true, completion: nil)
                }
            }
        })
    }


    // MARK: - Fetch Contacts, Containers, and Groups

    /// Fetches contacts, containers, and groups.
    fileprivate func fetchContainersContactsAndGroups() {
        fetchAllContainers()
        fetchAllContacts()
        fetchAllGroups()
    }

    /// Fetches all contacts, then updates all tabs accordingly.
    fileprivate func fetchAllContacts() {
        MGCContactStore.sharedInstance.fetchContacts(({(contacts: [CNContact]) in
            // true if there are one or more contacts, and false otherwise.
            self.didFindContacts = (contacts.count > 0) ? true : false

            self.refreshTabsDataModel(with: self.didFindContacts, with: self.didFindGroups, exchangeAccount: self.isExchangeAccount)

            // Notify the listener to refresh its UI.
            DispatchQueue.main.async {
                NotificationCenter.default.post(name: Notification.Name(rawValue: MGCAppConfiguration.MGCNotifications.refreshTab), object: self)
            }
        }))
    }

    /// Fetches all containers, then updates all tabs accordingly.
    fileprivate func fetchAllContainers() {
        MGCContactStore.sharedInstance.fetchContainers({(containers: [CNContainer]) in

            // Fetch all the container types. Remove any duplicate.
            let containerTypes = Array(Set(containers.map({(container: CNContainer) in container.nameMatchingContainerType})))

            // If we only have one container. We check whether it is an Exchange account.
            self.isExchangeAccount = (containerTypes.count == 1 && containerTypes.contains(MGCAppConfiguration.MainStoryboard.TableHeaderSection.Containers.exchange)) ? true : false

           self.refreshTabsDataModel(with: self.didFindContacts, with: self.didFindGroups, exchangeAccount: self.isExchangeAccount)

            // Notify the listener to refresh its UI.
            DispatchQueue.main.async {
                NotificationCenter.default.post(name: Notification.Name(rawValue: MGCAppConfiguration.MGCNotifications.refreshTab), object: self)
            }
        })
    }

    /// Fetches all groups, then updates all tabs accordingly.
    fileprivate func fetchAllGroups() {
        MGCContactStore.sharedInstance.fetchGroups({(groups: [CNGroup]) in
            // true if there are one or more groups, and false otherwise.
            self.didFindGroups = (groups.count > 0) ? true : false

            self.refreshTabsDataModel(with: self.didFindContacts, with: self.didFindGroups, exchangeAccount: self.isExchangeAccount)

            // Notify the listener to refresh its UI.
            DispatchQueue.main.async {
                NotificationCenter.default.post(name: Notification.Name(rawValue: MGCAppConfiguration.MGCNotifications.refreshTab), object: self)
            }
        })
    }


    // MARK: - Handle storeDidChangeNotification

    func handleStoreDidChangeNotification(_ notification: Notification) {
        fetchContainersContactsAndGroups()
    }


    // MARK: - Memory Management

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }


    // MARK: - Lifetime

    deinit {
        // Unregister for the storeDidChange notification.
        NotificationCenter.default.removeObserver(self, name: NSNotification.Name(rawValue: MGCAppConfiguration.MGCNotifications.storeDidChange), object: MGCContactStore.sharedInstance)
    }
}
```

[Next](ManagingContacts-ManagingContacts-SearchViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-MGCContactStore.swift.md)

