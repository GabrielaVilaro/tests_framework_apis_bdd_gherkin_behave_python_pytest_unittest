from behave import *
from functions.Functions import Functions

use_step_matcher("re")


class StepsDefinitions:

    @given('I connect with endpoint (.*)')
    def step_impl(self, host):
        self._endpoint = Functions.get_full_host(self, host)
        return self._endpoint

    @step("I do a Get")
    def step_impl(self):
        self._response = Functions.do_a_get(self)
        return self._response

    @step("I print out the results of the response")
    def step_impl(self):
        Functions.print_api_response(self)

    @then("The api response is (.*)")
    def step_impl(self, code):
        Functions.response_is(self, code)

    @step("I set the entity (.*) with the value (.*)")
    def step_impl(self, entity, value):
        Functions.set_body_values(self, entity, value)

    @when("I set the body with (.*)")
    def step_impl(self, file):
        Functions.set_initial_json_body(self, file)

    @when("I do a Put")
    def step_impl(self):
        Functions.do_a_put(self)

    @when("I do a Post")
    def step_impl(self):
        Functions.do_a_post(self)

    @step("I assert response in entity (.*) is (.*)")
    def step_impl(self, entity, expected):
        Functions.assert_response_expected(self, entity, expected)

    @step("I assert that response in entity (.*) path (.*) is (.*)")
    def step_impl(self, entity, subPath, expected):
        Functions.assert_response_expected(self, entity, expected, subPath)

    @step("The elements (.*) show the values (.*)")
    def step_impl(self, entity, expected):
        for row in self.table:
            entity = row['Entity']
            value = row['Value']
            Functions.assert_response_expected(self, entity, value)

    @step("elements (.*) in (.*) show the values (.*)")
    def step_impl(self, entity, subPath, expected):
        for row in self.table:
            print(row)
            entity = row['Entity']
            subPath = row['Path']
            value = row['Value']
            Functions.assert_response_expected(self, entity, value, subPath)

    @then("I compare the json File (.*) with response")
    def step_impl(self, file):
        Functions.expected_results_value(self, file)


