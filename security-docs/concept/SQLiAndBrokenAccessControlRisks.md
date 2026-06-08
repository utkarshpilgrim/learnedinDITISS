# SQL Injection and Broken Access Control Risks in DELETE Endpoints

### Vulnerability Context

`DELETE` operations are high-impact because successful exploitation affects data integrity and availability rather than simple data exfiltration. An attacker who can influence a DELETE endpoint may permanently remove records or disrupt application functionality.

### Authorization vs. Authentication

Authentication alone does not make an operation safe. Even when an authenticated administrator account triggers a delete action, the application must still verify that the user is authorized to delete the specific resource identified by the supplied parameter (commonly an id).

If the endpoint accepts an attacker-controlled id value without additional object-level checks, any authenticated user (or a compromised admin account) can target arbitrary records. This is a classic authorization failure—specifically a broken access control issue, often manifesting as Insecure Direct Object Reference (IDOR)—rather than an authentication bypass. The application correctly identifies the caller as authenticated and grants the general “delete” permission, but it fails to enforce granular access control on the target object.

### Mitigation Strategies

Two complementary controls are required:

- ***Parameterized queries (prepared statements)***: Use them for every database operation. User-supplied values (such as the id parameter) are bound as data only and cannot alter the SQL statement structure or logic. This directly prevents SQL injection.

- ***Least privilege at the database layer***: The database account used by the application must have only the minimum permissions needed.

### Database Least Privilege for Web Applications

Applications should never connect to the database using a privileged administrative account. Instead, use a dedicated service account with tightly scoped rights:

- Allowed operations are limited to the necessary CRUD actions on a small, explicitly defined set of tables.
- The account is explicitly denied the ability to:
    - Drop or alter tables and schema objects.
    - Access unrelated tables (audit logs, payment records, etc.).
    - Reach other databases or schemas on the same instance.
    - Create users, grant permissions, or execute administrative commands that could affect overall database state or availability.


### Summary

Combining parameterized queries with strict database least privilege significantly reduces both the likelihood of successful SQL injection and the impact of a compromised application account.
