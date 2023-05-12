Gem::Specification.new do |spec|
  spec.name          = "qcaster"
  spec.version       = "0.1.0"
  spec.authors       = ["wbnns"]
  spec.email         = ["hello@wbnns.com"]

  spec.summary       = %q{Schedule future casts on Farcaster}
  spec.description   = %q{Stop bothering everyone with your top of mind rants. Schedule them for the future.}
  spec.homepage      = "https://github.com/wbnns/qcaster"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0").reject { |f| f.match(%r{^(test|spec|features)/}) }
  spec.bindir        = "bin"
  spec.executables   = spec.files.grep(%r{^bin/}) { |f| File.basename(f) }
  spec.require_paths = ["lib"]

  spec.add_development_dependency "bundler", "~> 2.0"
  spec.add_development_dependency "rake", "~> 13.0"
  spec.add_development_dependency "rspec", "~> 3.0"
end

