from conans import ConanFile, CMake

class SystemShockConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    # Comma-separated list of requirements
    build_requires = [
        "sdl2_mixer/2.0.4@bincrafters/stable",
    ]
    generators = "cmake_find_package"

    def configure(self):
        # Disable unused dependencies
        self.options["sdl2"].shared = False
        if self.settings.os == "Linux":
            self.options["sdl2"].jack = False
            self.options["sdl2"].nas = False
            self.options["sdl2"].pulse = False
            self.options["sdl2_mixer"].tinymidi = False

        self.options["sdl2_mixer"].flac = False
        self.options["sdl2_mixer"].fluidsynth = False
        self.options["sdl2_mixer"].mad = False
        self.options["sdl2_mixer"].mikmod = False
        self.options["sdl2_mixer"].modplug = False
        self.options["sdl2_mixer"].mpg123 = False
        self.options["sdl2_mixer"].ogg = False
        self.options["sdl2_mixer"].opus = False
