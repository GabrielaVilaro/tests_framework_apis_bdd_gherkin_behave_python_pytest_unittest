# Created by gabrielavilaro at 11/07/2020

@Integration
Feature: Test WebApi

  @WebApi
  Scenario: GET pet data
    Given I connect with endpoint pet/Escenario:pet
    When I do a Get
    Then I print out the results of the response
    Then The api response is 200
    And I assert response in entity status is NOT NULL
    And I assert that response in entity category path id is 3
    And I assert that response in entity photoUrls path 0 is NOT NULL
    And I assert that response in entity tags path 0 is {'id': 1, 'name': 'Rita'}
    Then The elements <Entity> show the values <Value>
      | Entity | Value          |
      | id     | 501            |
      | name   | Luna           |
      | status | available      |
    Then elements <Entity> in <Path> show the values <Value>
      | Entity      |Path   | Value      |
      | category    |   id  | 3          |
      | photoUrls   |   0   | NOT NULL   |
    Then I compare the json File data_responses/pet501 with response

  @WebApi
  Scenario: Built Body Parameters Data
    Given I connect with endpoint pet
    Then I set the entity id with the value 501
    Then I set the entity name with the value Luna
    Then I set the entity status with the value available
    Then I set the entity email with the value random
    When I do a Post
    Then I print out the results of the response
    Then The api response is 200

  @WebApi
  Scenario: Get json as Body Parameters
    Given I connect with endpoint pet
    When I set the body with data_body/pet
    Then I set the entity id with the value 502
    Then I set the entity category with the value 'category': {'id': 2, 'name': 'Rosa'}
    Then I set the entity status with the value available
    Then I set the entity email with the value random
    When I do a Put
    Then I print out the results of the response

