# Application Access Tokens (OAuth)

Application access tokens are short-lived credentials which are issued by the authorisation server. It allows the client's application to act on behalf of the user (or itself) and call protected APIs. If stolen, an attacker can use the token to access the same APIs and resources the legitimate client was authorized for.

# OAuth 2.0 vs OpenID Connect (OIDC)

- OAuth 2.0 is an authorization framework. It answers the question: “Is this client allowed to perform this action on behalf of the user?” It does not provide user identity information.

- OpenID Connect (OIDC) is an identity layer built on top of OAuth 2.0. It answers: “Who is the user?” by adding an `id_token` that contains verified user claims.

### Real-world example

A to-do app wants to add or update events in a user’s Google Calendar.

- The app uses OIDC to authenticate the user (prove “this is Jane Doe”).
- The app then uses OAuth 2.0 to obtain permission (scope) to read/write the user’s calendar events.

OAuth uses `access_token` to authorise and OpenID Connect uses `id_token` to authenticate. Refer to [doc](https://auth0.com/blog/why-should-use-accesstokens-to-secure-an-api/) to learn more about it. 

| Aspect | id_token (OpenID Connect) | access_token (OAuth 2.0) |
| --- | --- | --- |
| Purpose | Authenticate the user’s identity | Authorize the client to call a specific API |
| Intended recipient | The client application | The resource server (API) |
| Format | Always a JWT (JSON Web Token) | Can be opaque or a JWT |
| Contains user info | Yes (name, email, picture, etc.) | Usually not (focuses on scopes and audience) |
| Audience (aud) claim | Client ID of the application | Identifier of the API(s) the token is valid for |
| Who decodes it | The client application | The API (the client treats it as opaque) |
| Typical lifetime | Short (minutes) | Short (minutes to hours) |

### Example `id_token`


```
{
  "iss": "http://${account.namespace}/",
  "sub": "auth0|123456",
  "aud": "${account.clientId}",
  "exp": 1311281970,
  "iat": 1311280970,
  "name": "Jane Doe",
  "given_name": "Jane",
  "family_name": "Doe",
  "gender": "female",
  "birthdate": "0000-10-31",
  "email": "janedoe@example.com",
  "picture": "http://example.com/janedoe/me.jpg"
}
```

You can see that the `aud` ensures it is issued for specific user only. 

### Example `access_token`(JWT)

```
{
  "iss": "https://${account.namespace}/",
  "sub": "auth0|123456",
  "aud": [
    "my-api-identifier",
    "https://${account.namespace}/userinfo"
  ],
  "azp": "${account.clientId}",
  "exp": 1489179954,
  "iat": 1489143954,
  "scope": "openid profile email address phone read:appointments email"
}
```

The client receives this token but does not parse it. It simply includes it in the `Authorization: Bearer <token>` header when calling the API.

### Key takeaway

1. Use the id_token when you need to know who the user is.
2. Use the access_token when you need to prove what your application is allowed to do.