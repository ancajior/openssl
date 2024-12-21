# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from absl.testing import absltest

import pathlib

media = pathlib.Path(__file__).parents[1] / "third_party"


class UnitTests(absltest.TestCase):
    def test_text_gen_text_only_prompt(self):
        # [START text_gen_text_only_prompt]
        import google.generativeai as genai

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content("Write a story about a magic backpack.")
        print(response.text)
        # [END text_gen_text_only_prompt]

    def test_text_gen_text_only_prompt_streaming(self):
        # [START text_gen_text_only_prompt_streaming]
        import google.generativeai as genai

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content("Write a story about a magic backpack.", stream=True)
        for chunk in response:
            print(chunk.text)
        # [END text_gen_text_only_prompt_streaming]