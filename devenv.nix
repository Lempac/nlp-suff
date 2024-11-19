{ pkgs, lib, config, inputs, ... }:

{
  packages = with pkgs; [ python312Packages.spacy python312Packages.spacy-transformers python312Packages.scikit-learn python312Packages.sentencepiece ];
  languages.python = {
    enable = true;
    venv.enable = true;
  };
}
