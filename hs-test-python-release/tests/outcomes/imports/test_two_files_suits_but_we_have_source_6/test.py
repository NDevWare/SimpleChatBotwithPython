from hstest import CheckResult, dynamic_test, StageTest, TestedProgram


class TestImportRelativeError2(StageTest):
    @dynamic_test
    def test(self):
        pr = TestedProgram('main2')
        return CheckResult(pr.start() == 'main2\n', '')
