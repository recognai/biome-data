from biome.data.sources import DataSource
import os

from tests import TESTS_BASEPATH
from tests.test_support import DaskSupportTest

FILES_PATH = os.path.join(TESTS_BASEPATH, "resources")


class ExcelDatasourceTest(DaskSupportTest):
    def test_read_excel(self):
        file_path = os.path.join(FILES_PATH, "test.xlsx")

        datasource = DataSource(format="xlsx", path=file_path)
        data_frame = datasource.to_dataframe().compute()

        assert len(data_frame) > 0
        self.assertTrue("path" in data_frame.columns)
