# pdfer
- CLI tool for merging and removing pages from PDF files.

# Setup

- Add `pdfer` to your `/usr/local/bin/`:
	- `sudo mv pdfer /usr/local/bin/`
- Make sure it is executable:
	- `sudo chmod +x /usr/local/bin/pdfer`

# Usage

- `pdfer [-h] -i [INPUT(S)] -o OUTPUT [-r [PAGES]] [-m]`
	- To merge `file1.pdf`, `file2.pdf`, and `file3.pdf` into `result.pdf` you would do `pdfer -m -i file1.pdf file2.pdf file3.pdf -o result.pdf`.
	- To remove pages 1, 2, and 5 from `file.pdf` and provide the result into `result.pdf` you would do `pdfer -r 1 2 5 -i file.pdf -o result.pdf`.
- For more details, do `pdfer -h`.
