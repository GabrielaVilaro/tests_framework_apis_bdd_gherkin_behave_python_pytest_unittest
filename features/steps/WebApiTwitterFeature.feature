# Created by gabrielavilaro at 19/07/2020

  @Twitter
Feature: Test Twitter

  @GetToken
  Scenario: Get Access token
    Given I connect with endpoint 1.1/search/tweets.json?q=from%3AEscenario:User_Test1&result_type=mixed&count=2
    When I login in Twitter App
    Then I do a Get
    And I print out the results of the response
    Then I compare response in entity statuses.created_at is NOT NULL
    Then I compare response in entity statuses.id is 1282630333343703041
    Then I compare response in entity statuses.entities.hashtags is []
    Then I compare response in entity statuses.entities.symbols is []
    Then I compare response in entity statuses.entities.user_mentions is []
    Then I compare response in entity statuses.entities.urls[0].url is https://t.co/9HRvkkMtAJ
    Then I compare <Entity> show the values <Value>
      | Entity                                              | Value                                                |
      | statuses.entities.urls[0].expanded_url              | https://twitter.com/i/web/status/1282630333343703041 |
      | statuses.entities.urls[0].display_url               | twitter.com/i/web/status/1…                          |