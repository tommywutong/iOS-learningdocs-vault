---
title: 'NavBar: Customizing UINavigationBar''s appearance'
apple_id: DTS40007418
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2017-12-07'
source_url: https://developer.apple.com/library/archive/samplecode/NavBar/Listings/NavBar_CitiesDataSource_swift.html
archived_at: '2026-07-18T03:16:52.816826Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [NavBar: Customizing UINavigationBar's appearance](NavBar-%20Customizing%20UINavigationBar%27s%20appearance.md)


[Next](NavBar-AppDelegate.swift.md)[Previous](NavBar-NavigationPrompt-NavigationPromptViewController.swift.md)

# NavBar/CitiesDataSource.swift

```swift
/*
Copyright (C) 2017 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Data source of city names.
*/

import Foundation
import UIKit

class CitiesDataSource: NSObject, UITableViewDataSource
{
    fileprivate var cities: [String] = []

    override init() {
        super.init()

        let citiesJSONURL =
            URL(fileURLWithPath: Bundle.main.path(forResource: "Cities", ofType: "json")!)
        do {
            let citiesJSONData = try Data(contentsOf: citiesJSONURL)
            let jsonObject = try JSONSerialization.jsonObject(with: citiesJSONData,
                                                              options: JSONSerialization.ReadingOptions(rawValue: UInt(0)))
            if let jsonCities = jsonObject as? [String] {
                cities = jsonCities
            }
        }
        catch {
            //..
        }
    }

    @objc func city(index: Int) -> String {
        return cities[index]
    }

    // MARK: - UITableViewDataSource

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return cities.count
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let flavor = cities[indexPath.row]
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
        cell.textLabel?.text = flavor
        return cell
    }

}
```

[Next](NavBar-AppDelegate.swift.md)[Previous](NavBar-NavigationPrompt-NavigationPromptViewController.swift.md)

