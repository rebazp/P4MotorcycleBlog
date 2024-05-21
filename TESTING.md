# Motorcycle Blog | Testing

Return to [README](README.md)
- - -
All testing for this project was conducted manually both during and after development. The anticipated outcomes of button clicks and feature tests are documented in this Testing.md file. This involved manually clicking buttons and links, and verifying that all functions performed as intended. All project functions are operational.

Django, a Python framework, was primarily used, with JavaScript handling the alert messages. These messages function correctly. Currently, Motorcycle Blog has no social media presence, so the links direct to their respective homepages.

As the project was developed using Bootstrap, it is fully responsive across all screen sizes.

## Table of Contents
* [Responsiveness Testing](#responsiveness-testing)
* [Browser Compatibility Testing](#browser-compatibility-testing)
* [Device Testing](#device-testing)
* [Code Validation](#code-validation)
* [HTML Validation](#html-validation)
* [CSS Testing](#css-testing)
* [Lighthouse Report](#lighthouse-report)
* [Bugs](#bugs)
* [Resolved Bugs](#resolved-bugs)
* [Unresolved Bugs](#unresolved-bugs)
* [Features Testing](#features-testing)

## Responsiveness Testing

* The deployed website underwent rigorous testing on multiple devices and screen sizes to ensure its responsiveness and adaptability. Developer Tools were utilized to simulate various screen sizes, enabling thorough examination of how the website behaves across different devices. Bootstrap classes and media queries were implemented to achieve the desired design, ensuring that the website maintains its visual and functional integrity on all platforms, enhancing the user experience.

![Am I Responsive](media/images/responsive.jpg)

## Browser Compatibility Testing

* The project was tested on multiple web browsers to check for compatibility issues and ensure it functions as expected across all of them. This testing process guarantees a smooth and consistent user experience, regardless of the browser used.

<details>
<summary> Chrome
</summary>

![Chrome](media/images/testing/browser/chrome.jpg)
</details>

<details>
<summary> Microsoft Edge
</summary>

![Microsoft Edge](media/images/testing/browser/microsoftedge.jpg)
</details>

<details>
<summary> Opera
</summary>

![Opera](media/images/testing/browser/opera.jpg)
</details>

<details>
<summary> Firefox
</summary>

![Firefox](media/images/testing/browser/firefox.jpg)
</details>

<details>
<summary> Samsung Internet (Mobile)
</summary>

![Samsung Internet Mobile](media/images/testing/browser/mobile.jpg)
</details>

## Device Testing

* Device testing was conducted on a variety of phone models, including Samsung Galaxy, iPhone and Sony. The assistance of family members and friends was sought to perform the testing. This comprehensive approach ensured that the website was thoroughly evaluated on different devices and platforms, contributing to a more robust and user-friendly final product.

## Code Validation

### HTML Validation

<details>
<summary> Home Page
</summary>

![Home Page](media/images/testing/code-validation/w3homeIndex.jpg)
</details>

<details>
<summary> Register Page
</summary>

![Register Page](media/images/testing/code-validation/w3signup.jpg)
- Since I'am using templates I cannot fix these errors.
</details>

<details>
<summary> Login Page
</summary>

![Login Page](media/images/testing/code-validation/w3login.jpg)
</details>

<details>
<summary> Logout Page
</summary>

![Logout Page](media/images/testing/code-validation/w3logout.jpg)
</details>

<details>
<summary> Add Post Page
</summary>

![Add Post Page](media/images/testing/code-validation/w3add_post.jpg)
</details>

<details>
<summary> View Posts Page
</summary>

![View Posts Page](media/images/testing/code-validation/w3post_list.jpg)
</details>

<details>
<summary> View Posts Detail Page
</summary>

![View Posts Detail Page](media/images/testing/code-validation/w3post_detail.jpg)
</details>

<details>
<summary> Edit Post Page
</summary>

![Edit Post Page](media/images/testing/code-validation/w3edit_post.jpg)
</details>

<details>
<summary> Delete Post Page
</summary>

![Delete Post Page](media/images/testing/code-validation/w3delete_post.jpg)
</details>

<details>
<summary> Edit Comment Page
</summary>

![Edit Comment Page](media/images/testing/code-validation/w3edit_comment.jpg)
</details>

<details>
<summary> Delete Comment Page
</summary>

![Delete Comment Page](media/images/testing/code-validation/w3comment_delete.jpg)
</details>

<details>
<summary> 404 Error Page
</summary>

![404 Error Page](media/images/testing/code-validation/w3404.jpg)
</details>

<details>
<summary> 500 Error Page
</summary>

![500 Error Page](media/images/testing/code-validation/w3500.jpg)
- Since I'am using templates with django I cannot fix these errors.
</details>

### CSS Testing

Testing with <https://jigsaw.w3.org/css-validator/> show no errors in CSS:

![Validator testing](media/images/testing/css.jpg)

## Lighthouse Report

<details>
<summary> Home Page
</summary>

![Home Page](media/images/testing/lighthouse/lhhome.jpg)
</details>

<details>
<summary> Register Page
</summary>

![Register Page](media/images/testing/lighthouse/lhsignup.jpg)
</details>

<details>
<summary> Login Page
</summary>

![Login Page](media/images/testing/lighthouse/lhlogin.jpg)
</details>

<details>
<summary> Logout Page
</summary>

![Logout Page](media/images/testing/lighthouse/lhlogout.jpg)
</details>

<details>
<summary> Add Post Page
</summary>

![Add Post Page](media/images/testing/lighthouse/lhaddpost.jpg)
</details>

<details>
<summary> View Posts Page
</summary>

![View Posts Page](media/images/testing/lighthouse/lhpostlist.jpg)
</details>

<details>
<summary> View Posts Detail Page
</summary>

![View Posts Detail Page](media/images/testing/lighthouse/lhpostdetail.jpg)
</details>

<details>
<summary> Edit Post Page
</summary>

![Edit Post Page](media/images/testing/lighthouse/lheditpost.jpg)
</details>

<details>
<summary> Delete Post Page
</summary>

![Delete Post Page](media/images/testing/lighthouse/lhdeletepost.jpg)
</details>

<details>
<summary> Edit Comment Page
</summary>

![Edit Comment Page](media/images/testing/lighthouse/lheditcomment.jpg)
</details>

<details>
<summary> Delete Comment Page
</summary>

![Delete Comment Page](media/images/testing/lighthouse/lhdeletecomment.jpg)
</details>

<details>
<summary> 404 Error Page
</summary>

![404 Error Page](media/images/testing/lighthouse/lherror404.jpg)
</details>

<details>
<summary> 500 Error Page
</summary>

![500 Error Page](media/images/testing/lighthouse/lherror500.jpg)
</details>

## Bugs

### Resolved Bugs

#### Remove Admin Approval

* When deleting a post or comment I didn't want the admins approval. I had some issues with the migrations not working properly and had to restart my IDE to solve the migration issue and managed to solved the bug.

#### Update Blog Post Text

* When editing the blog post the new text didn't appear for some reason. After asking the slack community I got the tip to check my models. I solved the bug by changing the post models and deleted the content function and kept body.

### Unresolved Bugs

* There are no unresolved bugs.

## Features Testing

![Features Testing Page 1](media/images/testing1.jpg)
![Features Testing Page 2](media/images/testing2.jpg)
