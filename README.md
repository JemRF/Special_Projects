# Special_Projects
### From: www.jemrf.com
##  SplashIDtoBW-csv.py
#  Format conversion tool to read SplashId CSV and generate a Bitwarden CSV import file.
=============================================================

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

 Glenn Seaton 2024
=============================================================
 The SplashIdtoBW-csv.py will convert all fields, but does not include any attached files for a SplashId record.
 It uses the standard SplashId CSV output.

 The field column names are lost when the CSV is created.
 The fields will be recreated as Field1, Field2, Field3, Field4, and Field5

 One additional field is the Date when that SplashId record was updated will have the imported field name "Last_Updated".

 I liked SplashId as a standalone tool and was using LastPass as my browser password tool. LastPass has limited extra field options and had problems with logging into domain subdomain. It would use the password for that domain and not the subdomain I was wanting.
