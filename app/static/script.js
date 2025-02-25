document.addEventListener("DOMContentLoaded", function () {
    // Handle form submission for client risk assessment
    document.getElementById("riskForm")?.addEventListener("submit", async function (event) {
        event.preventDefault();

        const clientId = document.getElementById("clientId").value;
        if (!clientId) {
            alert("Please enter a Client ID.");
            return;
        }

        try {
            const response = await fetch(`/compliance/check?client_id=${clientId}`);
            const data = await response.json();

            if (response.ok) {
                document.getElementById("riskScore").innerText = `Risk Score: ${data.risk_score}`;
            } else {
                alert(data.detail || "Error retrieving risk score.");
            }
        } catch (error) {
            console.error("Error fetching risk score:", error);
            alert("Failed to fetch risk data.");
        }
    });

    // Handle document upload to Azure Blob Storage
    document.getElementById("uploadForm")?.addEventListener("submit", async function (event) {
        event.preventDefault();

        const fileInput = document.getElementById("kycDocument");
        if (fileInput.files.length === 0) {
            alert("Please select a file to upload.");
            return;
        }

        const formData = new FormData();
        formData.append("file", fileInput.files[0]);

        try {
            const response = await fetch("/clients/upload", {
                method: "POST",
                body: formData
            });

            const data = await response.json();
            if (response.ok) {
                alert("File uploaded successfully.");
            } else {
                alert(data.detail || "Error uploading file.");
            }
        } catch (error) {
            console.error("Error uploading file:", error);
            alert("Failed to upload document.");
        }
    });
});
