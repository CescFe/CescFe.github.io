import os
import json
import unittest
from scripts.generate_collections import CollectionMarkdownGenerator


class TestCollectionMarkdownGenerator(unittest.TestCase):

    def setUp(self):
        self.test_dir = os.path.dirname(os.path.abspath(__file__))
        self.resources_dir = os.path.join(self.test_dir, 'resources', "collections")
        self.sample_json_path = os.path.join(self.resources_dir, 'sample_collections.json')
        self.output_dir = os.path.join(self.test_dir, '_test_collections')

        # Ensure the output directory exists
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def tearDown(self):
        # Remove the output directory after testing
        if os.path.exists(self.output_dir):
            for file in os.listdir(self.output_dir):
                file_path = os.path.join(self.output_dir, file)
                os.remove(file_path)
            os.rmdir(self.output_dir)

    def test_load_collections(self):
        generator = CollectionMarkdownGenerator(self.sample_json_path, "")
        collections = generator.load_collections()
        self.assertEqual(len(collections), 1)
        self.assertEqual(collections[0]['title'], "Sample Title")

    def test_create_markdown_content(self):
        with open(self.sample_json_path, 'r') as f:
            sample_data = json.load(f)
        collection = sample_data[0]
        content = CollectionMarkdownGenerator.create_markdown_content(collection)
        self.assertIn("title: Sample Title", content)

    def test_generate_markdown_files(self):
        generator = CollectionMarkdownGenerator(self.sample_json_path, self.output_dir)
        generator.generate_markdown_files()
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, "sample.md")))


if __name__ == '__main__':
    unittest.main()
