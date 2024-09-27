from qiskit_ibm_runtime import QiskitRuntimeService

# Save an IBM Quantum account and set it as your default account.
QiskitRuntimeService.save_account(
    channel="ibm_quantum",
    token="0964175ca1d3c383c1c9028e756c46fc04ab93e58a1a93fe671d6c8db253b6e7bd80a6bdf401363377fefacaed31775c9da8461f49433187acb4fbdb2fc394cc",
    set_as_default=True,
    # Use `overwrite=True` if you're updating your token.
    overwrite=True,
)

# Load saved credentials
service = QiskitRuntimeService()