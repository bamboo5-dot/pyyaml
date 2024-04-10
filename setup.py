---  # document start

# Comments in YAML look like this.
# YAML supports single-line comments.

################
# SCALAR TYPES #
################

# Our root object (which continues for the entire document) will be a map,
# which is equivalent to a dictionary, hash or object in other languages.
key: value
another_key: Another value goes here.
a_number_value: 100
scientific_notation: 1e+12
hex_notation: 0x123  # evaluates to 291
octal_notation: 0123 # evaluates to 83

# The number 1 will be interpreted as a number, not a boolean. 
# If you want it to be interpreted as a boolean, use true.
boolean: true
null_value: null
another_null_value: ~
key with spaces: value

# Yes and No (doesn't matter the case) will be evaluated to boolean 
# true and false values respectively.
# To use the actual value use single or double quotes.
no: no            # evaluates to "no": false
yes: No           # evaluates to "yes": false
not_enclosed: yes # evaluates to "not_enclosed": true
enclosed: "yes"   # evaluates to "enclosed": yes

# Notice that strings don't need to be quoted. However, they can be.
however: 'A string, enclosed in quotes.'
'Keys can be quoted too.': "Useful if you want to put a ':' in your key."
single quotes: 'have ''one'' escape pattern'
double quotes: "have many: \", \0, \t, \u263A, \x0d\x0a == \r\n, and more."
# UTF-8/16/32 characters need to be encoded
Superscript two: \u00B2

# Special characters must be enclosed in single or double quotes
special_characters: "[ John ] & { Jane } - <Doe>"

# Multiple-line strings can be written either as a 'literal block' (using |), 
# or a 'folded block' (using '>').
# Literal block turn every newline within the string into a literal newline (\n).
# Folded block removes newlines within the string.
literal_block: |
  This entire block of text will be the value of the 'literal_block' key,
  with line breaks being preserved.

  The literal continues until de-dented, and the leading indentation is
  stripped.

      Any lines that are 'more-indented' keep the rest of their indentation -
      these lines will be indented by 4 spaces.
folded_style: >
  This entire block of text will be the value of 'folded_style', but this
  time, all newlines will be replaced with a single space.

  Blank lines, like above, are converted to a newline character.

      'More-indented' lines keep their newlines, too -
      this text will appear over two lines.

# |- and >- removes the trailing blank lines (also called literal/block "strip")
literal_strip: |-
  This entire block of text will be the value of the 'literal_block' key,
  with trailing blank line being stripped.
block_strip: >-
  This entire block of text will be the value of 'folded_style', but this
  time, all newlines will be replaced with a single space and 
  trailing blank line being stripped.

# |+ and >+ keeps trailing blank lines (also called literal/block "keep")
literal_keep: |+
  This entire block of text will be the value of the 'literal_block' key,
  with trailing blank line being kept.

block_keep: >+
  This entire block of text will be the value of 'folded_style', but this
  time, all newlines will be replaced with a single space and 
  trailing blank line being kept.

####################
# COLLECTION TYPES #
####################

# Nesting uses indentation. 2 space indent is preferred (but not required).
a_nested_map:
  key: value
  another_key: Another Value
  another_nested_map:
    hello: hello

# Maps don't have to have string keys.
0.25: a float key

# Keys can also be complex, like multi-line objects
# We use ? followed by a space to indicate the start of a complex key.
? |
  This is a key
  that has multiple lines
: and this is its value

# YAML also allows mapping between sequences with the complex key syntax
# Some language parsers might complain
# An example
? - Manchester United
  - Real Madrid
: [ 2001-01-01, 2002-02-02 ]

# Sequences (equivalent to lists or arrays) look like this
# (note that the '-' counts as indentation):
a_sequence:
  - Item 1
  - Item 2
  - 0.5  # sequences can contain disparate types.
  - Item 4
  - key: value
    another_key: another_value
  - - This is a sequence
    - inside another sequence
  - - - Nested sequence indicators
      - can be collapsed

# Since YAML is a superset of JSON, you can also write JSON-style maps and
# sequences:
json_map: { "key": "value" }
json_seq: [ 3, 2, 1, "takeoff" ]
and quotes are optional: { key: [ 3, 2, 1, takeoff ] }

#######################
# EXTRA YAML FEATURES #
#######################

# YAML also has a handy feature called 'anchors', which let you easily duplicate
# content across your document.
# Anchors identified by & character which define the value.
# Aliases identified by * character which acts as "see above" command.
# Both of these keys will have the same value:
anchored_content: &anchor_name This string will appear as the value of two keys.
other_anchor: *anchor_name

# Anchors can be used to duplicate/inherit properties
base: &base
  name: Everyone has same name

# The expression << is called 'Merge Key Language-Independent Type'. It is used to
# indicate that all the keys of one or more specified maps should be inserted
# into the current map.
# NOTE: If key already exists alias will not be merged
foo:
  <<: *base # doesn't merge the anchor
  age: 10
  name: John
bar:
  <<: *base # base anchor will be merged
  age: 20

# foo and bar would also have name: Everyone has same name

# YAML also has tags, which you can use to explicitly declare types.
# Syntax: !![typeName] [value]
explicit_boolean: !!bool true
explicit_integer: !!int 42
explicit_float: !!float -42.24
explicit_string: !!str 0.5
explicit_datetime: !!timestamp 2022-11-17 12:34:56.78 +9
explicit_null: !!null null

# Some parsers implement language specific tags, like this one for Python's
# complex number type.
python_complex_number: !!python/complex 1+2j

# We can also use yaml complex keys with language specific tags
? !!python/tuple [ 5, 7 ]
: Fifty Seven
# Would be {(5, 7): 'Fifty Seven'} in Python

####################
# EXTRA YAML TYPES #
####################

# Strings and numbers aren't the only scalars that YAML can understand.
# ISO-formatted date and datetime literals are also parsed.
datetime_canonical: 2001-12-15T02:59:43.1Z
datetime_space_separated_with_time_zone: 2001-12-14 21:59:43.10 -5
date_implicit: 2002-12-14
date_explicit: !!timestamp 2002-12-14

# The !!binary tag indicates that a string is actually a base64-encoded
# representation of a binary blob.
gif_file: !!binary |
  R0lGODlhDAAMAIQAAP//9/X17unp5WZmZgAAAOfn515eXvPz7Y6OjuDg4J+fn5
  OTk6enp56enmlpaWNjY6Ojo4SEhP/++f/++f/++f/++f/++f/++f/++f/++f/+
  +f/++f/++f/++f/++f/++SH+Dk1hZGUgd2l0aCBHSU1QACwAAAAADAAMAAAFLC
  AgjoEwnuNAFOhpEMTRiggcz4BNJHrv/zCFcLiwMWYNG84BwwEeECcgggoBADs=

# YAML also has a set type, which looks like this:
set:
  ? item1
  ? item2
  ? item3
or: { item1, item2, item3 }

# Sets are just maps with null values; the above is equivalent to:
set2:
  item1: null
  item2: null
  item3: null

 # document end

NAME = 'PyYAML'
VERSION = '6.0.1'
DESCRIPTION = "YAML parser and emitter for Python"
LONG_DESCRIPTION = """\
YAML is a data serialization format designed for human readability
and interaction with scripting languages.  PyYAML is a YAML parser
and emitter for Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages.  PyYAML
supports standard YAML tags and provides Python-specific tags that
allow to represent an arbitrary Python object.

PyYAML is applicable for a broad range of tasks from complex
configuration files to object serialization and persistence."""
AUTHOR = "Kirill Simonov"
AUTHOR_EMAIL = 'xi@resolvent.net'
LICENSE = "MIT"
PLATFORMS = "Any"
URL = "https://pyyaml.org/"
DOWNLOAD_URL = "https://pypi.org/project/PyYAML/"
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Cython",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Text Processing :: Markup",
]
PROJECT_URLS = {
   'Bug Tracker': 'https://github.com/yaml/pyyaml/issues',
   'CI': 'https://github.com/yaml/pyyaml/actions',
   'Documentation': 'https://pyyaml.org/wiki/PyYAMLDocumentation',
   'Mailing lists': 'http://lists.sourceforge.net/lists/listinfo/yaml-core',
   'Source Code': 'https://github.com/yaml/pyyaml',
}

LIBYAML_CHECK = """
#include <yaml.h>

int main(void) {
    yaml_parser_t parser;
    yaml_emitter_t emitter;

    yaml_parser_initialize(&parser);
    yaml_parser_delete(&parser);

    yaml_emitter_initialize(&emitter);
    yaml_emitter_delete(&emitter);

    return 0;
}
"""


import sys, os, os.path, pathlib, platform, shutil, tempfile, warnings

# for newer setuptools, enable the embedded distutils before importing setuptools/distutils to avoid warnings
os.environ['SETUPTOOLS_USE_DISTUTILS'] = 'local'

from setuptools import setup, Command, Distribution as _Distribution, Extension as _Extension
from setuptools.command.build_ext import build_ext as _build_ext
# NB: distutils imports must remain below setuptools to ensure we use the embedded version
from distutils import log
from distutils.errors import DistutilsError, CompileError, LinkError, DistutilsPlatformError

with_cython = False
if 'sdist' in sys.argv or os.environ.get('PYYAML_FORCE_CYTHON') == '1':
    # we need cython here
    with_cython = True
try:
    from Cython.Distutils.extension import Extension as _Extension
    from Cython.Distutils import build_ext as _build_ext
    with_cython = True
except ImportError:
    if with_cython:
        raise

try:
    from wheel.bdist_wheel import bdist_wheel
except ImportError:
    bdist_wheel = None


# on Windows, disable wheel generation warning noise
windows_ignore_warnings = [
"Unknown distribution option: 'python_requires'",
"Config variable 'Py_DEBUG' is unset",
"Config variable 'WITH_PYMALLOC' is unset",
"Config variable 'Py_UNICODE_SIZE' is unset",
"Cython directive 'language_level' not set"
]

if platform.system() == 'Windows':
    for w in windows_ignore_warnings:
        warnings.filterwarnings('ignore', w)


class Distribution(_Distribution):
    def __init__(self, attrs=None):
        _Distribution.__init__(self, attrs)
        if not self.ext_modules:
            return
        for idx in range(len(self.ext_modules)-1, -1, -1):
            ext = self.ext_modules[idx]
            if not isinstance(ext, Extension):
                continue
            setattr(self, ext.attr_name, None)
            self.global_options = [
                    (ext.option_name, None,
                        "include %s (default if %s is available)"
                        % (ext.feature_description, ext.feature_name)),
                    (ext.neg_option_name, None,
                        "exclude %s" % ext.feature_description),
            ] + self.global_options
            self.negative_opt = self.negative_opt.copy()
            self.negative_opt[ext.neg_option_name] = ext.option_name

    def has_ext_modules(self):
        if not self.ext_modules:
            return False
        for ext in self.ext_modules:
            with_ext = self.ext_status(ext)
            if with_ext is None or with_ext:
                return True
        return False

    def ext_status(self, ext):
        implementation = platform.python_implementation()
        if implementation not in ['CPython', 'PyPy']:
            return False
        if isinstance(ext, Extension):
            # the "build by default" behavior is implemented by this returning None
            with_ext = getattr(self, ext.attr_name) or os.environ.get('PYYAML_FORCE_{0}'.format(ext.feature_name.upper()))
            try:
                with_ext = int(with_ext)  # attempt coerce envvar to int
            except TypeError:
                pass
            return with_ext
        else:
            return True


class Extension(_Extension):

    def __init__(self, name, sources, feature_name, feature_description,
            feature_check, **kwds):
        if not with_cython:
            for filename in sources[:]:
                base, ext = os.path.splitext(filename)
                if ext == '.pyx':
                    sources.remove(filename)
                    sources.append('%s.c' % base)
        _Extension.__init__(self, name, sources, **kwds)
        self.feature_name = feature_name
        self.feature_description = feature_description
        self.feature_check = feature_check
        self.attr_name = 'with_' + feature_name.replace('-', '_')
        self.option_name = 'with-' + feature_name
        self.neg_option_name = 'without-' + feature_name


class build_ext(_build_ext):

    def run(self):
        optional = True
        disabled = True
        for ext in self.extensions:
            with_ext = self.distribution.ext_status(ext)
            if with_ext is None:
                disabled = False
            elif with_ext:
                optional = False
                disabled = False
                break
        if disabled:
            return
        try:
            _build_ext.run(self)
        except DistutilsPlatformError:
            exc = sys.exc_info()[1]
            if optional:
                log.warn(str(exc))
                log.warn("skipping build_ext")
            else:
                raise

    def get_source_files(self):
        self.check_extensions_list(self.extensions)
        filenames = []
        for ext in self.extensions:
            if with_cython:
                self.cython_sources(ext.sources, ext)
            for filename in ext.sources:
                filenames.append(filename)
                base = os.path.splitext(filename)[0]
                for ext in ['c', 'h', 'pyx', 'pxd']:
                    filename = '%s.%s' % (base, ext)
                    if filename not in filenames and os.path.isfile(filename):
                        filenames.append(filename)
        return filenames

    def get_outputs(self):
        self.check_extensions_list(self.extensions)
        outputs = []
        for ext in self.extensions:
            fullname = self.get_ext_fullname(ext.name)
            filename = os.path.join(self.build_lib,
                                    self.get_ext_filename(fullname))
            if os.path.isfile(filename):
                outputs.append(filename)
        return outputs

    def build_extensions(self):
        self.check_extensions_list(self.extensions)
        for ext in self.extensions:
            with_ext = self.distribution.ext_status(ext)
            if with_ext is not None and not with_ext:
                continue
            if with_cython:
                ext.sources = self.cython_sources(ext.sources, ext)
            try:
                self.build_extension(ext)
            except (CompileError, LinkError):
                if with_ext is not None:
                    raise
                log.warn("Error compiling module, falling back to pure Python")


class test(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        warnings.warn('Running tests via `setup.py test` is deprecated and will be removed in a future release. Use `pytest` instead to ensure that the complete test suite is run.', DeprecationWarning)
        build_cmd = self.get_finalized_command('build')
        build_cmd.run()

        # running the tests this way can pollute the post-MANIFEST build sources
        # (see https://github.com/yaml/pyyaml/issues/527#issuecomment-921058344)
        # until we remove the test command, run tests from an ephemeral copy of the intermediate build sources
        tempdir = tempfile.TemporaryDirectory(prefix='test_pyyaml')

        try:
            # have to create a subdir since we don't get dir_exists_ok on copytree until 3.8
            temp_test_path = pathlib.Path(tempdir.name) / 'pyyaml'
            shutil.copytree(build_cmd.build_lib, temp_test_path)
            sys.path.insert(0, str(temp_test_path))
            sys.path.insert(0, 'tests/legacy_tests')

            import test_all
            if not test_all.main([]):
                raise DistutilsError("Tests failed")
        finally:
            try:
                # this can fail under Windows; best-effort cleanup
                tempdir.cleanup()
            except Exception:
                pass


cmdclass = {
    'build_ext': build_ext,
    'test': test,
}
if bdist_wheel:
    cmdclass['bdist_wheel'] = bdist_wheel


if __name__ == '__main__':

    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        license=LICENSE,
        platforms=PLATFORMS,
        url=URL,
        download_url=DOWNLOAD_URL,
        classifiers=CLASSIFIERS,
        project_urls=PROJECT_URLS,

        package_dir={'': 'lib'},
        packages=['yaml', '_yaml'],
        ext_modules=[
            Extension('yaml._yaml', ['yaml/_yaml.pyx'],
                'libyaml', "LibYAML bindings", LIBYAML_CHECK,
                libraries=['yaml']),
        ],

        distclass=Distribution,
        cmdclass=cmdclass,
        python_requires='>=3.6',
    )
