$(document).ready(function () {
  $("#hardware_table").DataTable({
    columnDefs: [
      {
        target: 8,
        searchable: false,
        orderable: false,
      },
      {
        target: 7,
        searchable: false,
        orderable: false,
      },
    ],
  });
});

var currentdate = new Date();
var report_file =
  currentdate.getFullYear() +
  "-" +
  (currentdate.getMonth() + 1) +
  "-" +
  currentdate.getDate() +
  "-" +
  currentdate.getHours() +
  "-" +
  currentdate.getMinutes() +
  "-" +
  currentdate.getSeconds() +
  ".txt";

// Generate Report function from form data on click and download the report
function generateReport() {
  var form = document.getElementById("reportForm");
  var formData = new FormData(form);
  var reportType = formData.get("report_type");
  var report = "";
  if (reportType == "1") {
    report = "Hardware-Report-" + report_file;
  } else if (reportType == "2") {
    report = "Software-Report-" + report_file;
  } else if (reportType == "3") {
    report = "Contract-Report-" + report_file;
  }

  var xhr = new XMLHttpRequest();
  xhr.open("POST", "", true);
  xhr.responseType = "blob";
  xhr.onload = function () {
    if (this.status === 200) {
      var blob = this.response;

      var link = document.createElement("a");
      link.href = window.URL.createObjectURL(blob);
      link.download = report;
      link.click();
    }
  };
  xhr.send(formData);
}

function openMoreDataModal(data) {
  $("#moreDataModal").modal("show");
  console.log(data);
  // var modal = document.getElementById("moreDataModal");
  // modal.style.display = "block";
  // var modalContent = document.getElementById("modal-content");

  // var modalData = document.createElement("p");
  // modalData.innerHTML = data;
  // modalContent.appendChild(modalData);

  // var span = document.getElementsByClassName("close")[0];
  // span.onclick = function () {
  //   modal.style.display = "none";
  //   modalContent.removeChild(modalData);
  // };
  // window.onclick = function (event) {
  //   if (event.target == modal) {
  //     modal.style.display = "none";
  //     modalContent.removeChild(modalData);
  //   }
  // };
}

function openDeleteModal(data) {
  $("#deleteDataModal").modal("show");
}

function openEditModal(data) {
  $("#editDataModal").modal("show");
}

function toggleDisableInput(formID, disableButtonID) {
  $(formID)
    .find("input")
    .each(function () {
      $(this).prop("disabled", !$(this).prop("disabled"));
    });
}

$(document).ready(function () {
  toggleDisableInput("#hardware_form");
  toggleDisableInput("#software_form");
  toggleDisableInput("#contract_form");

  var $form = $("#hardware_form"),
    origForm = $form.serialize();


    var $softwareform = $("#software_form"),
    origSoftwareForm = $form.serialize();

    var $contractform = $("#contract_form"),
    origContractForm = $form.serialize();

  $("form :input").on("change input", function (e) {
    $("#save_hardware").prop("disabled", origForm === $form.serialize());
  });
  $("form :input").on("change input", function (e) {
    $("#save_software").prop("disabled", origSoftwareForm === $softwareform.serialize());
  });
  $("form :input").on("change input", function (e) {
    $("#save_contract").prop("disabled", origContractForm === $contractform.serialize());
  });

});

const csrftoken = $('input[name="csrfmiddlewaretoken"]').val();

async function deleteHardware(id) {
  const request = new Request("delete/" + id, {
    method: "POST",
    headers: { "X-CSRFToken": csrftoken },
    mode: "same-origin", // Do not send CSRF token to another domain.
  });

  await fetch(request).then(function (response) {
    if (response.ok) {
      // If successful, direct to homepage
      window.location.href = "/inventory/hardwares";
    }
  });
}

function openSoftwareModal(...data) {
  console.log(data);
  modal = $("#softwareEditModal");
  $("#softwareId").val(data[0]);
  $("#softwareManfInput").val(data[1]);
  $("#softwareTitleInput").val(data[2]);
  $("#softwareDeviceInput").val(data[3]);
  $("#softwarePriceInput").val(parseInt(data[4]));

  modal.modal("show");
}

async function saveSoftware() {
  id = $("#softwareId").val();
  const request = new Request("softwares/", {
    method: "POST",
    headers: { "X-CSRFToken": csrftoken },
    mode: "same-origin", // Do not send CSRF token to another domain.
  });

  await fetch(request).then(function (response) {
    if (response.ok) {
      // If successful, direct to homepage
      window.location.href = "/inventory/softwares";
    }
  });
}

async function deleteSoftware(id) {
  const request = new Request("softwares/delete/" + id, {
    method: "POST",
    headers: { "X-CSRFToken": csrftoken },
    mode: "same-origin", // Do not send CSRF token to another domain.
  });
  console.log(request);
  await fetch(request).then(function (response) {
    if (response.ok) {
      // If successful, direct to homepage
      window.location.href = "/inventory/softwares";
    }
  });
}


async function saveContract() {
  id = $("#softwareId").val();
  const request = new Request("softwares/", {
    method: "POST",
    headers: { "X-CSRFToken": csrftoken },
    mode: "same-origin", // Do not send CSRF token to another domain.
  });

  await fetch(request).then(function (response) {
    if (response.ok) {
      // If successful, direct to homepage
      window.location.href = "/inventory/contracts";
    }
  });
}

async function deleteContract(id) {
  const request = new Request("contracts/delete/" + id, {
    method: "POST",
    headers: { "X-CSRFToken": csrftoken },
    mode: "same-origin", // Do not send CSRF token to another domain.
  });
  console.log(request);
  await fetch(request).then(function (response) {
    if (response.ok) {
      // If successful, direct to homepage
      window.location.href = "/inventory/contracts";
    }
  });
}

 async function downloadReport  (file_name) {
  // Create a request that passes the file name to the server by the body
  const request = new Request("report/download/"+file_name, {
    method: "GET",
    headers: { "X-CSRFToken": csrftoken, file_name: file_name },
    mode: "same-origin", // Do not send CSRF token to another domain.
  });



 await fetch(request).then(function (response) {
  response.headers.get("content-type")

    if (response.ok) {
      // download the file
      response.blob().then(function (blob) {
        var url = window.URL.createObjectURL(blob);
        var a = document.createElement("a");
        a.href = url;
        a.download = file_name;
        document.body.appendChild(a);
        a.click();
        a.remove();
      });
    }
  });
}

async function deleteReport(id) {
  const request = new Request("report/delete/" + id, {
    method: "POST",
    headers: { "X-CSRFToken": csrftoken },
    mode: "same-origin", // Do not send CSRF token to another domain.
  });
  console.log(request);
  await fetch(request).then(function (response) {
    if (response.ok) {
      // If successful, direct to homepage
      window.location.href = "/inventory/reports";
    }
  });
}
