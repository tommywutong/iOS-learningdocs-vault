---
title: Roster API
framework: Roster API
symbol_kind: module
role: collection
role_heading: Web Service
platforms: [Roster API 1.0.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/rosterapi
source_url: 'https://developer.apple.com/documentation/rosterapi'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/rosterapi.json'
content_hash: 'sha256:8a80b79b57657885'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Roster API

<sub>Web Service</sub>

Read information about people and classes from an Apple School Manager organization.

## Overview

Roster API provides access to people and class information in Apple School Manager (ASM). Use this REST API if you need to support a workflow within your app to automatically create student or teacher records in advance of the first day of school. A typical use case is when your app requires teachers to input assignments and due dates for students in each class.

Accessing the user and class information requires authorization from an administrator of the ASM organization. When you begin the Roster API authorization flow, use the scopes defined below to request the appropriate level of access:

- **`edu.users.read`** — Request read access to ASM users
- **`edu.classes.read`** — Request read access to ASM classes

At the end of the authorization flow, use the access token you receive to access the Roster API endpoints, which you use to fetch people and class information. For more information on requesting an access token, see [Token validation](signinwithapplerestapi/generate-and-validate-tokens.md).

Include the access token you receive in the Authorization header for every request. The Roster API associates the access token with an ASM organization. The endpoints return user and class information contained within that ASM organization. The unique account identifier from Sign in with Apple at Work & School is the same identifier provided in the Roster API user information. You may use this identifier to associate user information from the Roster API with a user signing in to your app.

## Topics

### Essentials

- [Obtaining information about people and classes](rosterapi/obtaining-information-about-people-and-classes.md) — Prepare your app to request organizational information from a server.
- [Validating with the Roster API test scope](rosterapi/validating-with-the-roster-api-test-scope.md) — Use test data to ensure your integration with the Roster API works correctly.

### Authentication

- [Integrating with Roster API and Sign in with Apple](rosterapi/integrating-with-roster-api-and-sign-in-with-apple.md) — Associate someone’s Managed Apple Account with their identity in Apple School Manager.

### Information about users

- [Read a user](rosterapi/returns-a-specific-user-in-an-apple-school-manager-organization.md) — Read a user in an Apple School Manager organization.
- [User](rosterapi/user.md) — A user in an Apple School Manager organization.
- [RoleLocation](rosterapi/rolelocation.md) — A mapping between a role assumed by a user in an Apple School Manager organization, and the corresponding location.
- [List users](rosterapi/returns-a-list-of-users-in-an-apple-school-manager-organization.md) — List users in an Apple School Manager organization.
- [List users in a class](rosterapi/returns-a-users-for-an-apple-school-manager-class.md) — List users in a class of an Apple School Manager organization.
- [Users](rosterapi/users.md) — A list of users, with a token for pagination.

### Information about classes

- [Read a class](rosterapi/returns-a-specific-class-in-an-apple-school-manager-organization..md) — Read a class from an Apple School Manager organization.
- [Class](rosterapi/class.md) — A class in an Apple School Manager organization.
- [List classes](rosterapi/returns-a-list-of-classes-for-an-apple-school-manager-organization.md) — List classes in an Apple School Manager organization.
- [Classes](rosterapi/classes.md) — A list of classes, with a token for pagination.

### Information about locations

- [Read a location](rosterapi/returns-a-specific-location-in-an-apple-school-manager-organization.md) — Returns a specific location in an Apple School Manager organization.
- [Location](rosterapi/location.md) — A location in an Apple School Manager organization.
- [List locations](rosterapi/returns-a-list-of-locations-for-an-apple-school-manager-organization.md) — Returns a list of locations in an Apple School Manager organization.
- [Locations](rosterapi/locations.md) — A list of locations, with a token for pagination.

### Information about the organization

- [Read the organization](rosterapi/returns-organization-infrmation.md) — Returns information about the Apple School Manager organization.
- [Organization](rosterapi/organization.md) — Information about an Apple School Manager organization.
- [Domain](rosterapi/domain.md) — A DNS domain name associated with an Apple School Manager organization.
