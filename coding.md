### Shared state in integration tests is usually problematic.

It leads to race conditions and other test code that are hard to untangle.  Creating new variables in tests is better.

  #### ❌ Bad Sharing
  ```csharp
  public const string _sharedProviderId;
  public void Test1()
  {
    var resource1 = CreateResource(_sharedProviderId);
    ...
  }
  public void Test2()
  {
    var resource2 = CreateResource(_sharedProviderId2);
    ...
  }
  ```

  #### ✅ Good
  ```csharp
  public string GenerateRandomProviderId() { ... } // Random or new GUID()
  
  public void Test1()
  {
    var providerId = GenerateNewProviderId();
    var resource = CreateResource(providerId1);
  }
  
  public void Test2()
  {
    var providerId = GenerateNewProviderId(); //
    var resource = CreateResource(providerId1);
  }
  ```
### If statements and other logic in tests are bad.

### Code that is "hard to test" is probably not well written.

### Being able to run and test code locally is important.  This seems trivial but depending on the repo or domain at Zocdoc, it is not always considered enough.

### In Integration tests, don't delete data in between runs. Data shouldn't have to be deleted in order for you test to work.
