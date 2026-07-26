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
translated: true
---

> 导航：[Technologies](technologies.md)

# Roster API

<sub>Web Service</sub>

从 Apple School Manager 组织中读取人员和班级信息。

## 概述

Roster API 提供对 Apple School Manager（ASM）中人员和班级信息的访问。如果你需要在开学第一天前，为 App 内的工作流提供自动创建学生或教师记录的支持，可使用此 REST API。一个典型用例是,你的 App 要求教师为每个班级的学生输入作业和截止日期。

访问用户和班级信息需要获得 ASM 组织管理员的授权。当你开始 Roster API 的授权流程时，请使用以下定义的作用域来请求相应级别的访问权限：

- **`edu.users.read`** — 请求对 ASM 用户的读取访问权限
- **`edu.classes.read`** — 请求对 ASM 班级的读取访问权限

在授权流程结束时，使用你收到的访问令牌来访问 Roster API 端点，用于获取人员和班级信息。有关请求访问令牌的更多信息，请参阅 [Token validation](signinwithapplerestapi/generate-and-validate-tokens.md)。

在每次请求的 Authorization 标头中包含你收到的访问令牌。Roster API 会将访问令牌与一个 ASM 组织相关联，端点返回的是该 ASM 组织内的用户和班级信息。「通过 Apple 在工作与学校环境登录」提供的唯一账户标识符，与 Roster API 用户信息中提供的标识符相同。你可以使用该标识符,将来自 Roster API 的用户信息与登录你的 App 的用户关联起来。

## 主题

### 要点

- [Obtaining information about people and classes](rosterapi/obtaining-information-about-people-and-classes.md) — 准备你的 App，以便从服务器请求组织信息。
- [Validating with the Roster API test scope](rosterapi/validating-with-the-roster-api-test-scope.md) — 使用测试数据确保你与 Roster API 的集成正常工作。

### 身份验证

- [Integrating with Roster API and Sign in with Apple](rosterapi/integrating-with-roster-api-and-sign-in-with-apple.md) — 将某人的 Managed Apple Account 与其在 Apple School Manager 中的身份相关联。

### 关于用户的信息

- [Read a user](rosterapi/returns-a-specific-user-in-an-apple-school-manager-organization.md) — 读取 Apple School Manager 组织中的一个用户。
- [User](rosterapi/user.md) — Apple School Manager 组织中的一个用户。
- [RoleLocation](rosterapi/rolelocation.md) — Apple School Manager 组织中用户所担任角色与对应地点之间的映射。
- [List users](rosterapi/returns-a-list-of-users-in-an-apple-school-manager-organization.md) — 列出 Apple School Manager 组织中的用户。
- [List users in a class](rosterapi/returns-a-users-for-an-apple-school-manager-class.md) — 列出 Apple School Manager 组织中某个班级的用户。
- [Users](rosterapi/users.md) — 用户列表，附带用于分页的令牌。

### 关于班级的信息

- [Read a class](rosterapi/returns-a-specific-class-in-an-apple-school-manager-organization..md) — 读取 Apple School Manager 组织中的一个班级。
- [Class](rosterapi/class.md) — Apple School Manager 组织中的一个班级。
- [List classes](rosterapi/returns-a-list-of-classes-for-an-apple-school-manager-organization.md) — 列出 Apple School Manager 组织中的班级。
- [Classes](rosterapi/classes.md) — 班级列表，附带用于分页的令牌。

### 关于地点的信息

- [Read a location](rosterapi/returns-a-specific-location-in-an-apple-school-manager-organization.md) — 返回 Apple School Manager 组织中的一个地点。
- [Location](rosterapi/location.md) — Apple School Manager 组织中的一个地点。
- [List locations](rosterapi/returns-a-list-of-locations-for-an-apple-school-manager-organization.md) — 返回 Apple School Manager 组织中的地点列表。
- [Locations](rosterapi/locations.md) — 地点列表，附带用于分页的令牌。

### 关于组织的信息

- [Read the organization](rosterapi/returns-organization-infrmation.md) — 返回 Apple School Manager 组织的信息。
- [Organization](rosterapi/organization.md) — 关于 Apple School Manager 组织的信息。
- [Domain](rosterapi/domain.md) — 与 Apple School Manager 组织相关联的 DNS 域名。
