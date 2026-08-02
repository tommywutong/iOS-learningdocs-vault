---
title: Simple UISearchBar with State Restoration
apple_id: DTS40007848
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2013-05-23'
source_url: https://developer.apple.com/library/archive/samplecode/TableSearch/Listings/TableSearch_APLViewController_m.html
archived_at: '2026-07-18T03:26:12.516479Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Simple UISearchBar with State Restoration](Simple%20UISearchBar%20with%20State%20Restoration.md)


[Next](TableSearch-APLDetailViewController.m.md)[Previous](TableSearch-APLProduct.m.md)

# TableSearch/APLViewController.m

```objc

/*
 Copyright (C) 2013-2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Main table view controller for the application.
 */

#import "APLViewController.h"
#import "APLProduct.h"


@interface APLViewController ()

/*
 The searchResults array contains the content filtered as a result of a search.
 */
@property (nonatomic) NSMutableArray *searchResults;

@end


@implementation APLViewController

#pragma mark - Lifecycle methods

- (void)viewDidLoad
{
    /*
     Create a mutable array to contain products for the search results table.
     */
    self.searchResults = [NSMutableArray arrayWithCapacity:[self.products count]];

    /*
     Set up the search scope buttons with titles using products' localized display names.
     */
    NSMutableArray *scopeButtonTitles = [[NSMutableArray alloc] init];
    [scopeButtonTitles addObject:NSLocalizedString(@"All", @"Title for the All button in the search display controller.")];

    for (NSString *deviceType in [APLProduct deviceTypeNames])
    {
        NSString *displayName = [APLProduct displayNameForType:deviceType];
        [scopeButtonTitles addObject:displayName];
    }

    self.searchDisplayController.searchBar.scopeButtonTitles = scopeButtonTitles;
}


-(void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    if ([segue.identifier isEqualToString:@"pushDetailView"])
    {
        // Sender is the table view cell.
        NSArray *sourceArray;
        NSIndexPath *indexPath = [self.searchDisplayController.searchResultsTableView indexPathForCell:(UITableViewCell *)sender];
        if (indexPath != nil)
        {
            sourceArray = self.searchResults;
        }
        else
        {
            indexPath = [self.tableView indexPathForCell:(UITableViewCell *)sender];
            sourceArray = self.products;
        }

        UIViewController *destinationController = segue.destinationViewController;
        APLProduct *product = sourceArray[indexPath.row];
        destinationController.title = product.name;
    }
}


#pragma mark - UITableView data source and delegate methods

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    /*
     If the requesting table view is the search display controller's table view, return the count of
     the filtered list, otherwise return the count of the main list.
     */
    if (tableView == self.searchDisplayController.searchResultsTableView)
    {
        return [self.searchResults count];
    }
    else
    {
        return [self.products count];
    }
}


- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *kCellID = @"CellIdentifier";

    // Dequeue a cell from self's table view.
    UITableViewCell *cell = [self.tableView dequeueReusableCellWithIdentifier:kCellID];

    /*
     If the requesting table view is the search display controller's table view, configure the cell using the search results array, otherwise use the product array.
     */
    APLProduct *product;

    if (tableView == self.searchDisplayController.searchResultsTableView)
    {
        product = [self.searchResults objectAtIndex:indexPath.row];
    }
    else
    {
        product = [self.products objectAtIndex:indexPath.row];
    }

    cell.textLabel.text = product.name;
    return cell;
}


#pragma mark - Content Filtering

- (void)updateFilteredContentForProductName:(NSString *)productName type:(NSString *)typeName
{
    /*
     Update the filtered array based on the search text and scope.
     */
    if ((productName == nil) || [productName length] == 0)
    {
        // If there is no search string and the scope is "All".
        if (typeName == nil)
        {
            self.searchResults = [self.products mutableCopy];
        }
        else
        {
            // If there is no search string and the scope is chosen.
            NSMutableArray *searchResults = [[NSMutableArray alloc] init];
            for (APLProduct *product in self.products)
            {
                if ([product.type isEqualToString:typeName])
                {
                    [searchResults addObject:product];
                }
            }
            self.searchResults = searchResults;
        }
        return;
    }


    [self.searchResults removeAllObjects]; // First clear the filtered array.
    /*
     Search the main list for products whose type matches the scope (if selected) and whose name matches searchText; add items that match to the filtered array.
     */
    for (APLProduct *product in self.products)
    {
        if ((typeName == nil) || [product.type isEqualToString:typeName])
        {
            NSUInteger searchOptions = NSCaseInsensitiveSearch | NSDiacriticInsensitiveSearch;
            NSRange productNameRange = NSMakeRange(0, product.name.length);
            NSRange foundRange = [product.name rangeOfString:productName options:searchOptions range:productNameRange];
            if (foundRange.length > 0)
            {
                [self.searchResults addObject:product];
            }
        }
    }
}


#pragma mark - UISearchDisplayController Delegate Methods

- (BOOL)searchDisplayController:(UISearchDisplayController *)controller shouldReloadTableForSearchString:(NSString *)searchString
{
    NSString *scope;

    NSInteger selectedScopeButtonIndex = [self.searchDisplayController.searchBar selectedScopeButtonIndex];
    if (selectedScopeButtonIndex > 0)
    {
        scope = [[APLProduct deviceTypeNames] objectAtIndex:(selectedScopeButtonIndex - 1)];
    }

    [self updateFilteredContentForProductName:searchString type:scope];

    // Return YES to cause the search result table view to be reloaded.
    return YES;
}


- (BOOL)searchDisplayController:(UISearchDisplayController *)controller shouldReloadTableForSearchScope:(NSInteger)searchOption
{
    NSString *searchString = [self.searchDisplayController.searchBar text];
    NSString *scope;

    if (searchOption > 0)
    {
        scope = [[APLProduct deviceTypeNames] objectAtIndex:(searchOption - 1)];
    }

    [self updateFilteredContentForProductName:searchString type:scope];

    // Return YES to cause the search result table view to be reloaded.
    return YES;
}


#pragma mark - State restoration

static NSString *SearchDisplayControllerIsActiveKey = @"SearchDisplayControllerIsActiveKey";
static NSString *SearchBarScopeIndexKey = @"SearchBarScopeIndexKey";
static NSString *SearchBarTextKey = @"SearchBarTextKey";
static NSString *SearchBarIsFirstResponderKey = @"SearchBarIsFirstResponderKey";

static NSString *SearchDisplayControllerSelectedRowKey = @"SearchDisplayControllerSelectedRowKey";
static NSString *TableViewSelectedRowKey = @"TableViewSelectedRowKey";


- (void)encodeRestorableStateWithCoder:(NSCoder *)coder
{
    [super encodeRestorableStateWithCoder:coder];

    UISearchDisplayController *searchDisplayController = self.searchDisplayController;

    BOOL searchDisplayControllerIsActive = [searchDisplayController isActive];
    [coder encodeBool:searchDisplayControllerIsActive forKey:SearchDisplayControllerIsActiveKey];

    if (searchDisplayControllerIsActive)
    {
        [coder encodeObject:[searchDisplayController.searchBar text] forKey:SearchBarTextKey];
        [coder encodeInteger:[searchDisplayController.searchBar selectedScopeButtonIndex] forKey:SearchBarScopeIndexKey];

        NSIndexPath *selectedIndexPath = [searchDisplayController.searchResultsTableView indexPathForSelectedRow];
        if (selectedIndexPath != nil)
        {
            [coder encodeObject:selectedIndexPath forKey:SearchDisplayControllerSelectedRowKey];
        }

        BOOL searchFieldIsFirstResponder = [searchDisplayController.searchBar isFirstResponder];
        [coder encodeBool:searchFieldIsFirstResponder forKey:SearchBarIsFirstResponderKey];
    }

    NSIndexPath *selectedIndexPath = [self.tableView indexPathForSelectedRow];
    if (selectedIndexPath != nil)
    {
        [coder encodeObject:selectedIndexPath forKey:TableViewSelectedRowKey];
    }
}


- (void)decodeRestorableStateWithCoder:(NSCoder *)coder
{
    [super decodeRestorableStateWithCoder:coder];

    BOOL searchDisplayControllerIsActive = [coder decodeBoolForKey:SearchDisplayControllerIsActiveKey];

    if (searchDisplayControllerIsActive)
    {
        [self.searchDisplayController setActive:YES];

        /*
         Order is important here. Setting the search bar text causes searchDisplayController:shouldReloadTableForSearchString: to be invoked.
         */
        NSInteger searchBarScopeIndex = [coder decodeIntegerForKey:SearchBarScopeIndexKey];
        [self.searchDisplayController.searchBar setSelectedScopeButtonIndex:searchBarScopeIndex];

        NSString *searchBarText = [coder decodeObjectForKey:SearchBarTextKey];
        if (searchBarText != nil)
        {
            [self.searchDisplayController.searchBar setText:searchBarText];
        }

        NSIndexPath *selectedIndexPath = [coder decodeObjectForKey:SearchDisplayControllerSelectedRowKey];
        if (selectedIndexPath != nil)
        {
            [self.searchDisplayController.searchResultsTableView selectRowAtIndexPath:selectedIndexPath animated:NO scrollPosition:UITableViewScrollPositionTop];
        }

        BOOL searchFieldIsFirstResponder = [coder decodeBoolForKey:SearchBarIsFirstResponderKey];
        if (searchFieldIsFirstResponder)
        {
            [self.searchDisplayController.searchBar becomeFirstResponder];
        }

    }
    NSIndexPath *selectedIndexPath = [coder decodeObjectForKey:TableViewSelectedRowKey];
    if (selectedIndexPath != nil)
    {
        [self.tableView selectRowAtIndexPath:selectedIndexPath animated:NO scrollPosition:UITableViewScrollPositionTop];
    }
}


@end
```

[Next](TableSearch-APLDetailViewController.m.md)[Previous](TableSearch-APLProduct.m.md)

